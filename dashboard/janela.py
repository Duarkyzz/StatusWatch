"""Coordenação das telas originais, com operações em segundo plano."""

import sys
from datetime import datetime
from PySide6.QtCore import QTimer
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QStackedWidget,
    QMessageBox,
    QPushButton,
    QLineEdit,
    QHBoxLayout,
    QComboBox,
    QSpinBox,
    QCheckBox,
    QTableWidgetItem,
    QFileDialog,
    QHeaderView,
)
from app import database
from app.monitor import verificar_url, normalizar_url
from app.export import exportar_csv
from dashboard.pages import LoginPage, CadastroPage, DashboardPage
from dashboard.styles import STYLE
from dashboard.workers import Task


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.usuario_atual = None
        self.historico = []
        self.ultimos = []
        self.task = None
        self.busy = False
        self.setWindowTitle("StatusWatch • Monitoramento")
        self.resize(1280, 800)
        self.setMinimumSize(1100, 760)
        self.pilha = QStackedWidget()
        self.login, self.cadastro, self.dashboard = (
            LoginPage(),
            CadastroPage(),
            DashboardPage(),
        )
        for page in (self.login, self.cadastro, self.dashboard):
            self.pilha.addWidget(page)
        self.setCentralWidget(self.pilha)
        self.login.botao_cadastro.clicked.connect(self.abrir_cadastro)
        self.cadastro.botao_voltar.clicked.connect(self.abrir_login)
        self.dashboard.botao_sair.clicked.connect(self.realizar_logout)
        self.login.botao_login.clicked.connect(self.realizar_login)
        self.login.input_senha_login.returnPressed.connect(self.realizar_login)
        self.cadastro.botao_cadastrar.clicked.connect(self.realizar_cadastro)
        self.cadastro.input_confirmacao.returnPressed.connect(self.realizar_cadastro)
        self.dashboard.botao_adicionar.clicked.connect(self.adicionar_monitor)
        self.dashboard.input_url.returnPressed.connect(self.adicionar_monitor)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.verificar_todos)
        self.criar_opcoes()
        self.statusBar().showMessage("Pronto • Entre para acessar seus serviços")

    def criar_opcoes(self):
        d = self.dashboard
        d.dashboard_titulo.setText("Visão geral")
        d.servicos_titulo.setText("Seus serviços • última verificação de cada URL")
        d.card_offline.label_titulo.setText("Com falha")
        d.card_online.label_valor.setStyleSheet("color: #59d6ae")
        d.card_offline.label_valor.setStyleSheet("color: #ff909d")
        d.historico_subtitulo.setText(
            "Até 1.000 verificações recentes da sua conta. Datas no horário local."
        )
        d.botao_adicionar.setText("Verificar URL")
        self.atualizar = QPushButton("Atualizar histórico")
        self.rever = QPushButton("Verificar todos")
        self.auto = QCheckBox("Automático")
        self.intervalo = QSpinBox()
        self.intervalo.setRange(30, 3600)
        self.intervalo.setValue(60)
        self.intervalo.setSuffix(" s")
        self.intervalo.setToolTip(
            "Intervalo entre rodadas, enquanto o programa estiver aberto."
        )
        line = QHBoxLayout()
        for widget in (self.rever, self.atualizar, self.auto, self.intervalo):
            line.addWidget(widget)
        d.monitor_card.layout().addLayout(line)
        self.atualizar.clicked.connect(self.carregar_historico)
        self.rever.clicked.connect(self.verificar_todos)
        self.auto.toggled.connect(self.configurar_timer)
        self.intervalo.valueChanged.connect(self.configurar_timer)
        self.busca = QLineEdit()
        self.busca.setPlaceholderText("Buscar por URL ou mensagem de status…")
        self.filtro = QComboBox()
        self.filtro.addItems(["Todos", "Online", "Com falha"])
        self.exportar = QPushButton("Exportar CSV")
        bar = QHBoxLayout()
        for widget in (self.busca, self.filtro, self.exportar):
            bar.addWidget(widget)
        d.pagina_historico.layout().insertLayout(2, bar)
        self.busca.textChanged.connect(self.filtrar_historico)
        self.filtro.currentTextChanged.connect(self.filtrar_historico)
        self.exportar.clicked.connect(self.exportar_historico)
        for table in (d.tabela_servicos, d.tabela_historico):
            table.setShowGrid(False)
            table.verticalHeader().setDefaultSectionSize(44)
            header = table.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.ResizeMode.Interactive)
            header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
            for col, width in [(1, 185), (2, 65), (3, 90), (4, 190)]:
                table.setColumnWidth(col, width)
        for page, field in [
            (self.login, self.login.input_senha_login),
            (self.cadastro, self.cadastro.input_senha_cadastro),
        ]:
            show = QCheckBox("Mostrar senha")
            show.toggled.connect(
                lambda checked, f=field: f.setEchoMode(
                    QLineEdit.EchoMode.Normal
                    if checked
                    else QLineEdit.EchoMode.Password
                )
            )
            card = page.card_login if page is self.login else page.card_cadastro
            card.layout().insertWidget(card.layout().count() - 2, show)
        self.cadastro.input_senha_cadastro.setPlaceholderText("Pelo menos 8 caracteres")

    def executar(self, operation, callback, message):
        if self.busy:
            return
        self.busy = True
        self.statusBar().showMessage(message)
        # Impede outra sessão/operação enquanto a tarefa atual está em andamento.
        for widget in (
            self.login,
            self.cadastro,
            self.dashboard.botao_sair,
            self.dashboard.botao_adicionar,
            self.rever,
            self.atualizar,
        ):
            widget.setEnabled(False)
        self.task = Task(operation, self)
        self.task.success.connect(callback)
        self.task.failure.connect(self.erro)
        self.task.finished.connect(self.finalizar_tarefa)
        self.task.start()

    def finalizar_tarefa(self):
        for widget in (
            self.login,
            self.cadastro,
            self.dashboard.botao_sair,
            self.dashboard.botao_adicionar,
            self.rever,
            self.atualizar,
        ):
            widget.setEnabled(True)
        self.busy = False
        self.task.deleteLater()
        self.task = None

    def erro(self, message):
        self.auto.setChecked(False)
        self.statusBar().showMessage("Operação não concluída • tente novamente")
        QMessageBox.warning(self, "StatusWatch", message)

    def realizar_login(self):
        if self.busy:
            return
        email, senha = (
            self.login.input_email_login.text(),
            self.login.input_senha_login.text(),
        )
        if not email.strip() or not senha:
            self.erro("Digite seu e-mail e sua senha.")
            return

        def operation():
            user = database.fazer_login(email, senha)
            if user is None:
                return None
            return (
                user,
                database.buscar_historico(user["id"]),
                database.buscar_ultimos(user["id"]),
            )

        self.executar(
            operation, self.login_concluido, "Entrando e carregando seus serviços…"
        )

    def login_concluido(self, result):
        self.login.input_senha_login.clear()
        if result is None:
            self.erro("E-mail ou senha incorretos.")
            return
        self.usuario_atual, history, latest = result
        self.pilha.setCurrentWidget(self.dashboard)
        self.dashboard.abrir_dashboard()
        self.dashboard.dashboard_subtitulo.setText(
            f"{self.usuario_atual['email']} • Monitoramento de sites e APIs"
        )
        self.aplicar_dados((history, latest))

    def realizar_cadastro(self):
        if self.busy:
            return
        c = self.cadastro
        email, senha = c.input_email_cadastro.text(), c.input_senha_cadastro.text()
        if senha != c.input_confirmacao.text():
            self.erro("As senhas digitadas não são iguais.")
            return
        self.executar(
            lambda: database.cadastrar_usuario(email, senha),
            self.cadastro_concluido,
            "Criando sua conta…",
        )

    def cadastro_concluido(self, message):
        if message != "Cadastro criado com sucesso!":
            self.erro(message)
            return
        self.login.input_email_login.setText(
            self.cadastro.input_email_cadastro.text().strip()
        )
        for field in (
            self.cadastro.input_email_cadastro,
            self.cadastro.input_senha_cadastro,
            self.cadastro.input_confirmacao,
        ):
            field.clear()
        self.abrir_login()
        self.statusBar().showMessage("Conta criada • entre com sua senha")

    def carregar_historico(self):
        if not self.usuario_atual or self.busy:
            return
        uid = self.usuario_atual["id"]
        self.executar(
            lambda: (database.buscar_historico(uid), database.buscar_ultimos(uid)),
            self.aplicar_dados,
            "Carregando histórico…",
        )

    def adicionar_monitor(self):
        if not self.usuario_atual or self.busy:
            return
        try:
            url = normalizar_url(self.dashboard.input_url.text())
        except ValueError as e:
            self.erro(str(e))
            return
        self.verificar_lista([url])

    def verificar_todos(self):
        if not self.usuario_atual or self.busy:
            return
        urls = [row[1] for row in self.ultimos]
        if not urls:
            self.statusBar().showMessage("Adicione uma URL para começar a monitorar.")
            return
        self.verificar_lista(urls)

    def verificar_lista(self, urls):
        uid = self.usuario_atual["id"]

        def operation():
            for url in urls:
                if self.task.isInterruptionRequested():
                    break
                database.salvar_verificacao(verificar_url(url), uid)
            return database.buscar_historico(uid), database.buscar_ultimos(uid)

        self.executar(
            operation, self.aplicar_dados, f"Verificando {len(urls)} serviço(s)…"
        )

    def aplicar_dados(self, data):
        self.historico, self.ultimos = data
        self.preencher_tabela(self.dashboard.tabela_servicos, self.ultimos)
        self.filtrar_historico()
        online = sum(row[3] == "Online" for row in self.ultimos)
        self.dashboard.card_monitorados.label_valor.setText(str(len(self.ultimos)))
        self.dashboard.card_online.label_valor.setText(str(online))
        self.dashboard.card_offline.label_valor.setText(str(len(self.ultimos) - online))
        message = (
            "Adicione sua primeira URL acima."
            if not self.ultimos
            else f"Atualizado às {datetime.now():%H:%M:%S} • {len(self.ultimos)} serviço(s)"
        )
        self.statusBar().showMessage(message)

    def historico_filtrado(self):
        search = self.busca.text().strip().casefold()
        filtro = self.filtro.currentText()
        return [
            r
            for r in self.historico
            if search in f"{r[1]} {r[3]}".casefold()
            and (filtro == "Todos" or (r[3] == "Online") == (filtro == "Online"))
        ]

    def filtrar_historico(self):
        self.preencher_tabela(
            self.dashboard.tabela_historico, self.historico_filtrado()
        )

    def preencher_tabela(self, table, rows):
        table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            _, url, code, status, elapsed, date = row
            if isinstance(date, datetime):
                date = date.astimezone().strftime("%d/%m/%Y %H:%M:%S")
            values = [
                url,
                status,
                str(code) if code is not None else "—",
                f"{elapsed:.2f} s" if elapsed is not None else "—",
                str(date or "—"),
            ]
            for j, value in enumerate(values):
                item = QTableWidgetItem(value)
                item.setToolTip(value)
                if j == 1:
                    item.setForeground(
                        QColor("#59d6ae" if status == "Online" else "#ff909d")
                    )
                table.setItem(i, j, item)

    def exportar_historico(self):
        rows = self.historico_filtrado()
        if not rows:
            self.statusBar().showMessage("Nenhum resultado para exportar.")
            return
        path, _ = QFileDialog.getSaveFileName(
            self,
            "Exportar resultados filtrados",
            "statuswatch-historico.csv",
            "CSV (*.csv)",
        )
        if path:
            try:
                exportar_csv(path, rows)
                self.statusBar().showMessage(f"{len(rows)} verificações exportadas.")
            except OSError:
                self.erro(
                    "Não foi possível salvar. Escolha uma pasta com permissão de escrita."
                )

    def configurar_timer(self, *_):
        self.timer.stop()
        if self.auto.isChecked() and self.usuario_atual:
            self.timer.start(self.intervalo.value() * 1000)
            self.statusBar().showMessage(
                "Monitoramento automático ativo enquanto esta sessão estiver aberta."
            )

    def realizar_logout(self):
        if self.busy:
            return
        self.auto.setChecked(False)
        self.timer.stop()
        self.usuario_atual = None
        self.historico, self.ultimos = [], []
        self.busca.clear()
        self.filtro.setCurrentIndex(0)
        self.aplicar_dados(([], []))
        self.dashboard.input_url.clear()
        self.abrir_login()
        self.statusBar().showMessage("Sessão encerrada")

    def abrir_login(self):
        self.pilha.setCurrentWidget(self.login)

    def abrir_cadastro(self):
        self.pilha.setCurrentWidget(self.cadastro)

    def closeEvent(self, event):
        if self.busy:
            self.task.requestInterruption()
            self.auto.setChecked(False)
            self.statusBar().showMessage(
                "Aguarde a operação atual terminar e feche novamente."
            )
            event.ignore()
        else:
            event.accept()


def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setStyleSheet(STYLE)
    window = MainWindow()
    window.show()
    if "--smoke-test" in sys.argv:
        QTimer.singleShot(400, app.quit)
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
