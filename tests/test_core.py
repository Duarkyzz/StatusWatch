import hashlib
import csv
from contextlib import contextmanager
from unittest.mock import MagicMock
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread
import pytest
import requests
from app import database, config
from app.monitor import verificar_url, normalizar_url
from app.security import gerar_hash, verificar_senha
from app.export import exportar_csv


@pytest.mark.parametrize(
    "url,expected",
    [
        (" example.com ", "https://example.com/"),
        ("HTTPS://EXAMPLE.com/a#b", "https://example.com/a"),
        ("http://127.0.0.1:8080/api?x=1", "http://127.0.0.1:8080/api?x=1"),
    ],
)
def test_normalizar(url, expected):
    assert normalizar_url(url) == expected


@pytest.mark.parametrize(
    "url",
    [
        "",
        "https://",
        "ftp://example.com",
        "a b",
        "https://u:p@example.com",
        "https://abc:99999",
    ],
)
def test_invalid_url(url):
    with pytest.raises(ValueError):
        normalizar_url(url)


def test_password_compatibility():
    hashed = gerar_hash("senha-forte")
    assert hashed != gerar_hash("senha-forte")
    assert verificar_senha("senha-forte", hashed)
    assert not verificar_senha("errada", hashed)
    assert verificar_senha("antiga", hashlib.sha256(b"antiga").hexdigest())
    assert not verificar_senha("x", "pbkdf2_sha256$bad")


@pytest.mark.parametrize(
    "exception,status",
    [
        (requests.exceptions.Timeout(), "Servidor demorou demais"),
        (requests.exceptions.SSLError(), "Erro no certificado"),
        (requests.exceptions.ConnectionError(), "Não foi possível"),
    ],
)
def test_network_errors(monkeypatch, exception, status):
    def fail(*a, **k):
        raise exception

    monkeypatch.setattr(requests, "get", fail)
    result = verificar_url("https://example.com")
    assert result["status"].startswith(status)
    assert result["status_code"] is None
    assert result["response_time"] >= 0


def test_real_http_server():
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(int(self.path.strip("/")))
            self.end_headers()

        def log_message(self, *args):
            pass

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    worker = Thread(target=server.serve_forever, daemon=True)
    worker.start()
    try:
        for code in (200, 201, 204, 404, 500):
            result = verificar_url(f"http://127.0.0.1:{server.server_port}/{code}")
            assert result["status_code"] == code
            assert (result["status"] == "Online") == (code < 400)
    finally:
        server.shutdown()
        server.server_close()
        worker.join()


@pytest.fixture
def cursor(monkeypatch):
    cur = MagicMock()

    @contextmanager
    def connection():
        yield cur

    monkeypatch.setattr(database, "conectar", connection)
    return cur


def test_login_migrates_legacy(cursor):
    cursor.fetchone.return_value = (7, hashlib.sha256(b"antiga").hexdigest())
    assert database.fazer_login(" TEST@EXAMPLE.COM ", "antiga")["id"] == 7
    sql, params = cursor.execute.call_args.args
    assert sql.startswith("UPDATE") and params[1] == 7
    assert verificar_senha("antiga", params[0])


def test_wrong_password_does_not_update(cursor):
    cursor.fetchone.return_value = (7, gerar_hash("correta"))
    assert database.fazer_login("test@example.com", "errada") is None
    assert cursor.execute.call_count == 1


def test_signup_validation_and_duplicate(cursor):
    assert "válido" in database.cadastrar_usuario("bad", "12345678")
    assert "8 caracteres" in database.cadastrar_usuario("a@b.com", "123")
    cursor.execute.assert_not_called()
    cursor.execute.side_effect = database.psycopg2.errors.UniqueViolation()
    assert database.cadastrar_usuario("a@b.com", "12345678") == "E-mail já cadastrado."


def test_history_is_scoped(cursor):
    database.buscar_historico(42)
    sql, params = cursor.execute.call_args.args
    assert "WHERE usuario_id = %s" in sql and params == (42,)
    assert "LIMIT 1000" in sql
    database.buscar_ultimos(42)
    sql, params = cursor.execute.call_args.args
    assert "DISTINCT ON (url)" in sql and params == (42,)


def test_save_is_scoped(cursor):
    database.salvar_verificacao(
        dict(url="https://a/", status_code=200, status="Online", response_time=0.1), 42
    )
    assert cursor.execute.call_args.args[1][0] == 42
    with pytest.raises(ValueError):
        database.salvar_verificacao({}, None)


def test_connection_closes_on_failure(monkeypatch):
    conn = MagicMock()
    monkeypatch.setattr(database.psycopg2, "connect", lambda *a, **k: conn)
    with pytest.raises(RuntimeError):
        with database.conectar():
            raise RuntimeError("test")
    conn.close.assert_called_once()
    assert conn.__exit__.call_args.args[0] == RuntimeError


def test_env_independent_of_cwd(tmp_path, monkeypatch):
    monkeypatch.delenv("DATABASE_URL")
    monkeypatch.setattr(config, "BASE_DIR", tmp_path)
    (tmp_path / ".env").write_text("DATABASE_URL=postgresql://example")
    monkeypatch.chdir(tmp_path.parent)
    assert config.database_url() == "postgresql://example"


def test_csv(tmp_path):
    path = tmp_path / "history.csv"
    exportar_csv(path, [(1, "https://a/?x=1;2", None, "=1+1", 0.2, None)])
    with path.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.reader(f, delimiter=";"))
    assert rows[1][1] == "https://a/?x=1;2"
    assert rows[1][3] == "'=1+1"
