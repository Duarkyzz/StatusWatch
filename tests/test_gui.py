import time
from datetime import datetime, timezone
from PySide6.QtTest import QTest
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMessageBox
import pytest
from app import database
from dashboard import janela

ROWS = [
    (2, "https://example.com/", 200, "Online", 0.2, datetime.now(timezone.utc)),
    (
        1,
        "https://broken.com/",
        500,
        "Status HTTP: 500",
        0.3,
        datetime.now(timezone.utc),
    ),
]


def wait(window, qtapp):
    deadline = time.monotonic() + 5
    while window.busy and time.monotonic() < deadline:
        qtapp.processEvents()
        QTest.qWait(5)
    assert not window.busy


@pytest.fixture
def window(qtapp, monkeypatch):
    monkeypatch.setattr(QMessageBox, "warning", lambda *a: None)
    w = janela.MainWindow()
    w.show()
    yield w
    wait(w, qtapp)
    w.close()


def authenticate(window, qtapp, monkeypatch):
    monkeypatch.setattr(
        database, "fazer_login", lambda *a: {"id": 7, "email": "a@b.com"}
    )
    monkeypatch.setattr(database, "buscar_historico", lambda uid: ROWS)
    monkeypatch.setattr(database, "buscar_ultimos", lambda uid: ROWS)
    window.login.input_email_login.setText("a@b.com")
    window.login.input_senha_login.setText("password")
    window.login.botao_login.click()
    wait(window, qtapp)


def test_login_filter_export_logout(window, qtapp, monkeypatch, tmp_path):
    authenticate(window, qtapp, monkeypatch)
    assert window.pilha.currentWidget() is window.dashboard
    assert window.dashboard.card_online.label_valor.text() == "1"
    assert window.login.input_senha_login.text() == ""
    window.filtro.setCurrentText("Com falha")
    assert window.dashboard.tabela_historico.rowCount() == 1
    window.busca.setText("nonexistent")
    assert window.dashboard.tabela_historico.rowCount() == 0
    window.busca.clear()
    path = str(tmp_path / "out.csv")
    monkeypatch.setattr(janela.QFileDialog, "getSaveFileName", lambda *a: (path, "CSV"))
    window.exportar_historico()
    assert "broken.com" in (tmp_path / "out.csv").read_text()
    window.auto.setChecked(True)
    assert window.timer.isActive()
    window.realizar_logout()
    assert not window.timer.isActive()
    assert window.usuario_atual is None and not window.historico
    assert window.dashboard.tabela_servicos.rowCount() == 0


def test_ui_remains_responsive_and_prevents_duplicates(window, qtapp, monkeypatch):
    count = []

    def delayed(*a):
        count.append(1)
        time.sleep(0.15)
        return None

    monkeypatch.setattr(database, "fazer_login", delayed)
    window.login.input_email_login.setText("a@b.com")
    window.login.input_senha_login.setText("password")
    ticks = []
    timer = QTimer()
    timer.timeout.connect(lambda: ticks.append(1))
    timer.start(10)
    window.realizar_login()
    window.realizar_login()
    assert not window.close()  # A thread não é destruída durante execução.
    wait(window, qtapp)
    timer.stop()
    assert len(ticks) >= 3 and len(count) == 1
    assert window.usuario_atual is None


def test_signup_navigation(window, qtapp, monkeypatch):
    monkeypatch.setattr(
        database, "cadastrar_usuario", lambda *a: "Cadastro criado com sucesso!"
    )
    window.login.botao_cadastro.click()
    assert window.pilha.currentWidget() is window.cadastro
    c = window.cadastro
    c.input_email_cadastro.setText("a@b.com")
    c.input_senha_cadastro.setText("password")
    c.input_confirmacao.setText("password")
    c.botao_cadastrar.click()
    wait(window, qtapp)
    assert window.pilha.currentWidget() is window.login
    assert window.login.input_email_login.text() == "a@b.com"
    assert c.input_senha_cadastro.text() == ""


def test_monitor_uses_logged_in_user(window, qtapp, monkeypatch):
    authenticate(window, qtapp, monkeypatch)
    calls = []
    monkeypatch.setattr(janela, "verificar_url", lambda url: {"url": url})
    monkeypatch.setattr(
        database, "salvar_verificacao", lambda result, uid: calls.append((result, uid))
    )
    window.dashboard.input_url.setText("example.com")
    window.dashboard.botao_adicionar.click()
    wait(window, qtapp)
    assert calls == [({"url": "https://example.com/"}, 7)]
    window.verificar_todos()
    wait(window, qtapp)
    assert len(calls) == 3


def test_failure_restores_controls(window, qtapp, monkeypatch):
    def fail(*a):
        raise RuntimeError("private credentials")

    monkeypatch.setattr(database, "fazer_login", fail)
    messages = []
    monkeypatch.setattr(QMessageBox, "warning", lambda *a: messages.append(a[-1]))
    window.login.input_email_login.setText("a@b.com")
    window.login.input_senha_login.setText("password")
    window.realizar_login()
    wait(window, qtapp)
    assert window.login.isEnabled()
    assert messages and "private credentials" not in messages[0]
