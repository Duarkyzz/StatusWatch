
import sys

from app.database import cadastrar_usuario, fazer_login

from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QStackedWidget,
    QFrame,
    QTableWidget,
    QHeaderView,
    QAbstractItemView,
    QGraphicsOpacityEffect,
    QMessageBox
)


# ==========================================================
# TELA DE LOGIN
# ==========================================================

class LoginPage(QWidget):

    def __init__(self):
        super().__init__()

        layout_principal = QVBoxLayout(self)

        layout_principal.setContentsMargins(
            40,
            40,
            40,
            40
        )

        layout_principal.addStretch()

        # --------------------------------------------------
        # Card de login
        # --------------------------------------------------

        self.card_login = QFrame()
        self.card_login.setObjectName("authCard")
        self.card_login.setFixedWidth(420)

        layout_card = QVBoxLayout(self.card_login)

        layout_card.setContentsMargins(
            36,
            36,
            36,
            36
        )

        layout_card.setSpacing(14)

        # --------------------------------------------------
        # Título
        # --------------------------------------------------

        self.titulo = QLabel("StatusWatch")
        self.titulo.setObjectName("authTitle")

        self.titulo.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        # --------------------------------------------------
        # Subtítulo
        # --------------------------------------------------

        self.subtitulo = QLabel(
            "Monitore seus sites e serviços em um só lugar."
        )

        self.subtitulo.setObjectName("authSubtitle")

        self.subtitulo.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.subtitulo.setWordWrap(True)

        # --------------------------------------------------
        # Campo de e-mail
        # --------------------------------------------------

        self.label_email_login = QLabel("E-mail")
        self.label_email_login.setObjectName("fieldLabel")

        self.input_email_login = QLineEdit()

        self.input_email_login.setPlaceholderText(
            "seuemail@exemplo.com"
        )

        # --------------------------------------------------
        # Campo de senha
        # --------------------------------------------------

        self.label_senha_login = QLabel("Senha")
        self.label_senha_login.setObjectName("fieldLabel")

        self.input_senha_login = QLineEdit()

        self.input_senha_login.setPlaceholderText(
            "Digite sua senha"
        )

        self.input_senha_login.setEchoMode(
            QLineEdit.EchoMode.Password
        )

        # --------------------------------------------------
        # Botão de login
        # --------------------------------------------------

        self.botao_login = QPushButton("Entrar")
        self.botao_login.setObjectName("primaryButton")

        self.botao_login.setCursor(
            Qt.CursorShape.PointingHandCursor
        )

        # --------------------------------------------------
        # Botão de cadastro
        # --------------------------------------------------

        self.botao_cadastro = QPushButton(
            "Criar uma conta"
        )

        self.botao_cadastro.setObjectName("linkButton")

        self.botao_cadastro.setCursor(
            Qt.CursorShape.PointingHandCursor
        )

        # --------------------------------------------------
        # Adicionando elementos ao card
        # --------------------------------------------------

        layout_card.addWidget(self.titulo)
        layout_card.addWidget(self.subtitulo)

        layout_card.addSpacing(14)

        layout_card.addWidget(self.label_email_login)
        layout_card.addWidget(self.input_email_login)

        layout_card.addWidget(self.label_senha_login)
        layout_card.addWidget(self.input_senha_login)

        layout_card.addSpacing(8)

        layout_card.addWidget(self.botao_login)
        layout_card.addWidget(self.botao_cadastro)

        layout_principal.addWidget(
            self.card_login,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        layout_principal.addStretch()


# ==========================================================
# TELA DE CADASTRO
# ==========================================================

class CadastroPage(QWidget):

    def __init__(self):
        super().__init__()

        layout_principal = QVBoxLayout(self)

        layout_principal.setContentsMargins(
            40,
            40,
            40,
            40
        )

        layout_principal.addStretch()

        # --------------------------------------------------
        # Card de cadastro
        # --------------------------------------------------

        self.card_cadastro = QFrame()
        self.card_cadastro.setObjectName("authCard")
        self.card_cadastro.setFixedWidth(420)

        layout_card = QVBoxLayout(
            self.card_cadastro
        )

        layout_card.setContentsMargins(
            36,
            36,
            36,
            36
        )

        layout_card.setSpacing(14)

        # --------------------------------------------------
        # Título
        # --------------------------------------------------

        self.titulo = QLabel("Criar conta")
        self.titulo.setObjectName("authTitle")

        self.titulo.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        # --------------------------------------------------
        # Subtítulo
        # --------------------------------------------------

        self.subtitulo = QLabel(
            "Crie sua conta para começar a monitorar seus serviços."
        )

        self.subtitulo.setObjectName("authSubtitle")

        self.subtitulo.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.subtitulo.setWordWrap(True)

        # --------------------------------------------------
        # Campo de e-mail
        # --------------------------------------------------

        self.label_email_cadastro = QLabel("E-mail")
        self.label_email_cadastro.setObjectName("fieldLabel")

        self.input_email_cadastro = QLineEdit()

        self.input_email_cadastro.setPlaceholderText(
            "seuemail@exemplo.com"
        )

        # --------------------------------------------------
        # Campo de senha
        # --------------------------------------------------

        self.label_senha_cadastro = QLabel("Senha")
        self.label_senha_cadastro.setObjectName("fieldLabel")

        self.input_senha_cadastro = QLineEdit()

        self.input_senha_cadastro.setPlaceholderText(
            "Digite sua senha"
        )

        self.input_senha_cadastro.setEchoMode(
            QLineEdit.EchoMode.Password
        )

        # --------------------------------------------------
        # Confirmação de senha
        # --------------------------------------------------

        self.label_confirmacao = QLabel(
            "Confirme sua senha"
        )

        self.label_confirmacao.setObjectName("fieldLabel")

        self.input_confirmacao = QLineEdit()

        self.input_confirmacao.setPlaceholderText(
            "Digite sua senha novamente"
        )

        self.input_confirmacao.setEchoMode(
            QLineEdit.EchoMode.Password
        )

        # --------------------------------------------------
        # Botão cadastrar
        # --------------------------------------------------

        self.botao_cadastrar = QPushButton(
            "Cadastrar"
        )

        self.botao_cadastrar.setObjectName(
            "primaryButton"
        )

        self.botao_cadastrar.setCursor(
            Qt.CursorShape.PointingHandCursor
        )

        # --------------------------------------------------
        # Botão voltar
        # --------------------------------------------------

        self.botao_voltar = QPushButton(
            "Voltar para o login"
        )

        self.botao_voltar.setObjectName(
            "linkButton"
        )

        self.botao_voltar.setCursor(
            Qt.CursorShape.PointingHandCursor
        )

        # --------------------------------------------------
        # Adicionando elementos
        # --------------------------------------------------

        layout_card.addWidget(self.titulo)
        layout_card.addWidget(self.subtitulo)

        layout_card.addSpacing(14)

        layout_card.addWidget(
            self.label_email_cadastro
        )

        layout_card.addWidget(
            self.input_email_cadastro
        )

        layout_card.addWidget(
            self.label_senha_cadastro
        )

        layout_card.addWidget(
            self.input_senha_cadastro
        )

        layout_card.addWidget(
            self.label_confirmacao
        )

        layout_card.addWidget(
            self.input_confirmacao
        )

        layout_card.addSpacing(8)

        layout_card.addWidget(
            self.botao_cadastrar
        )

        layout_card.addWidget(
            self.botao_voltar
        )

        layout_principal.addWidget(
            self.card_cadastro,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        layout_principal.addStretch()


# ==========================================================
# CARD DE ESTATÍSTICA
# ==========================================================

class StatCard(QFrame):

    def __init__(self, titulo, valor):
        super().__init__()

        self.setObjectName("statCard")

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            22,
            18,
            22,
            18
        )

        layout.setSpacing(4)

        self.label_titulo = QLabel(titulo)
        self.label_titulo.setObjectName("statTitle")

        self.label_valor = QLabel(valor)
        self.label_valor.setObjectName("statValue")

        layout.addWidget(self.label_titulo)
        layout.addWidget(self.label_valor)


# ==========================================================
# TELA DO DASHBOARD
# ==========================================================

class DashboardPage(QWidget):

    def __init__(self):
        super().__init__()

        layout_principal = QHBoxLayout(self)

        layout_principal.setContentsMargins(
            0,
            0,
            0,
            0
        )

        layout_principal.setSpacing(0)

        # ==================================================
        # MENU LATERAL
        # ==================================================

        self.sidebar = QFrame()
        self.sidebar.setObjectName("sidebar")
        self.sidebar.setFixedWidth(220)

        sidebar_layout = QVBoxLayout(
            self.sidebar
        )

        sidebar_layout.setContentsMargins(
            22,
            28,
            22,
            28
        )

        sidebar_layout.setSpacing(10)

        # --------------------------------------------------
        # Logo / nome
        # --------------------------------------------------

        self.logo = QLabel("StatusWatch")
        self.logo.setObjectName("sidebarLogo")

        sidebar_layout.addWidget(self.logo)
        sidebar_layout.addSpacing(30)

        # --------------------------------------------------
        # Navegação
        # --------------------------------------------------

        self.menu_dashboard = QPushButton(
            "Dashboard"
        )

        self.menu_dashboard.setObjectName(
            "navButtonActive"
        )

        self.menu_dashboard.setCursor(
            Qt.CursorShape.PointingHandCursor
        )

        self.menu_historico = QPushButton(
            "Histórico"
        )

        self.menu_historico.setObjectName(
            "navButton"
        )

        self.menu_historico.setCursor(
            Qt.CursorShape.PointingHandCursor
        )

        sidebar_layout.addWidget(
            self.menu_dashboard
        )

        sidebar_layout.addWidget(
            self.menu_historico
        )

        sidebar_layout.addStretch()

        # --------------------------------------------------
        # Botão sair
        # --------------------------------------------------

        self.botao_sair = QPushButton("Sair")
        self.botao_sair.setObjectName("logoutButton")

        self.botao_sair.setCursor(
            Qt.CursorShape.PointingHandCursor
        )

        sidebar_layout.addWidget(
            self.botao_sair
        )

        # ==================================================
        # CONTEÚDO PRINCIPAL
        # ==================================================

        self.conteudo = QWidget()

        conteudo_layout = QVBoxLayout(
            self.conteudo
        )

        conteudo_layout.setContentsMargins(
            34,
            30,
            34,
            30
        )

        conteudo_layout.setSpacing(22)

        # --------------------------------------------------
        # Cabeçalho
        # --------------------------------------------------

        self.dashboard_titulo = QLabel(
            "Dashboard"
        )

        self.dashboard_titulo.setObjectName(
            "pageTitle"
        )

        self.dashboard_subtitulo = QLabel(
            "Acompanhe o status dos seus serviços."
        )

        self.dashboard_subtitulo.setObjectName(
            "pageSubtitle"
        )

        conteudo_layout.addWidget(
            self.dashboard_titulo
        )

        conteudo_layout.addWidget(
            self.dashboard_subtitulo
        )

        # ==================================================
        # CARDS DE ESTATÍSTICA
        # ==================================================

        stats_layout = QHBoxLayout()
        stats_layout.setSpacing(16)

        self.card_monitorados = StatCard(
            "Monitorados",
            "0"
        )

        self.card_online = StatCard(
            "Online",
            "0"
        )

        self.card_offline = StatCard(
            "Offline",
            "0"
        )

        stats_layout.addWidget(
            self.card_monitorados
        )

        stats_layout.addWidget(
            self.card_online
        )

        stats_layout.addWidget(
            self.card_offline
        )

        conteudo_layout.addLayout(
            stats_layout
        )

        # ==================================================
        # CADASTRAR URL
        # ==================================================

        self.monitor_card = QFrame()
        self.monitor_card.setObjectName("contentCard")

        monitor_layout = QVBoxLayout(
            self.monitor_card
        )

        monitor_layout.setContentsMargins(
            22,
            20,
            22,
            20
        )

        monitor_layout.setSpacing(12)

        self.monitor_titulo = QLabel(
            "Adicionar monitor"
        )

        self.monitor_titulo.setObjectName(
            "sectionTitle"
        )

        monitor_layout.addWidget(
            self.monitor_titulo
        )

        url_layout = QHBoxLayout()
        url_layout.setSpacing(10)

        self.input_url = QLineEdit()

        self.input_url.setPlaceholderText(
            "https://exemplo.com"
        )

        self.botao_adicionar = QPushButton(
            "Adicionar"
        )

        self.botao_adicionar.setObjectName(
            "primaryButton"
        )

        self.botao_adicionar.setFixedWidth(130)

        self.botao_adicionar.setCursor(
            Qt.CursorShape.PointingHandCursor
        )

        url_layout.addWidget(
            self.input_url
        )

        url_layout.addWidget(
            self.botao_adicionar
        )

        monitor_layout.addLayout(
            url_layout
        )

        conteudo_layout.addWidget(
            self.monitor_card
        )

        # ==================================================
        # TABELA DE SERVIÇOS
        # ==================================================

        self.servicos_card = QFrame()
        self.servicos_card.setObjectName(
            "contentCard"
        )

        servicos_layout = QVBoxLayout(
            self.servicos_card
        )

        servicos_layout.setContentsMargins(
            22,
            20,
            22,
            20
        )

        servicos_layout.setSpacing(14)

        self.servicos_titulo = QLabel(
            "Serviços monitorados"
        )

        self.servicos_titulo.setObjectName(
            "sectionTitle"
        )

        servicos_layout.addWidget(
            self.servicos_titulo
        )

        self.tabela_servicos = QTableWidget()

        self.tabela_servicos.setColumnCount(5)

        self.tabela_servicos.setHorizontalHeaderLabels(
            [
                "URL",
                "Status",
                "HTTP",
                "Resposta",
                "Última verificação"
            ]
        )

        self.tabela_servicos.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )

        self.tabela_servicos.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )

        self.tabela_servicos.verticalHeader().setVisible(
            False
        )

        self.tabela_servicos.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        servicos_layout.addWidget(
            self.tabela_servicos
        )

        conteudo_layout.addWidget(
            self.servicos_card
        )

        layout_principal.addWidget(
            self.sidebar
        )

        layout_principal.addWidget(
            self.conteudo
        )


# ==========================================================
# JANELA PRINCIPAL
# ==========================================================

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # --------------------------------------------------
        # Configurações da janela
        # --------------------------------------------------

        self.setWindowTitle(
            "StatusWatch"
        )

        self.resize(
            1200,
            700
        )

        self.setMinimumSize(
            1000,
            600
        )

        # --------------------------------------------------
        # Pilha de páginas
        # --------------------------------------------------

        self.pilha = QStackedWidget()

        # --------------------------------------------------
        # Criando páginas
        # --------------------------------------------------

        self.login = LoginPage()
        self.cadastro = CadastroPage()
        self.dashboard = DashboardPage()

        # --------------------------------------------------
        # Adicionando páginas à pilha
        # --------------------------------------------------

        self.pilha.addWidget(
            self.login
        )

        self.pilha.addWidget(
            self.cadastro
        )

        self.pilha.addWidget(
            self.dashboard
        )

        self.setCentralWidget(
            self.pilha
        )

        # --------------------------------------------------
        # Navegação
        # --------------------------------------------------

        self.login.botao_cadastro.clicked.connect(
            self.abrir_cadastro
        )

        self.cadastro.botao_voltar.clicked.connect(
            self.abrir_login
        )

        self.dashboard.botao_sair.clicked.connect(
            self.realizar_logout
        )

        # --------------------------------------------------
        # Banco de dados
        # --------------------------------------------------

        self.login.botao_login.clicked.connect(
            self.realizar_login
        )

        self.cadastro.botao_cadastrar.clicked.connect(
            self.realizar_cadastro
        )

        # ENTER também executa login/cadastro
        self.login.input_senha_login.returnPressed.connect(
            self.realizar_login
        )

        self.cadastro.input_confirmacao.returnPressed.connect(
            self.realizar_cadastro
        )

    # ======================================================
    # CADASTRO
    # ======================================================

    def realizar_cadastro(self):

        email = (
            self.cadastro
            .input_email_cadastro
            .text()
            .strip()
        )

        senha = (
            self.cadastro
            .input_senha_cadastro
            .text()
        )

        confirmacao = (
            self.cadastro
            .input_confirmacao
            .text()
        )

        # --------------------------------------------------
        # Campos vazios
        # --------------------------------------------------

        if not email or not senha or not confirmacao:

            QMessageBox.warning(
                self,
                "Campos incompletos",
                "Preencha todos os campos."
            )

            return

        # --------------------------------------------------
        # Confirmação de senha
        # --------------------------------------------------

        if senha != confirmacao:

            QMessageBox.warning(
                self,
                "Senhas diferentes",
                "As senhas digitadas não são iguais."
            )

            self.cadastro.input_senha_cadastro.clear()
            self.cadastro.input_confirmacao.clear()

            self.cadastro.input_senha_cadastro.setFocus()

            return

        # --------------------------------------------------
        # Banco de dados
        # --------------------------------------------------

        try:

            resultado = cadastrar_usuario(
                email,
                senha
            )

            print(
                f"Resultado do cadastro: {resultado}"
            )

            # A função pode retornar False
            if resultado is False:

                QMessageBox.warning(
                    self,
                    "Cadastro",
                    "Não foi possível criar a conta."
                )

                return

            # A função também pode retornar uma mensagem
            if isinstance(resultado, str):

                resultado_lower = resultado.lower()

                mensagens_erro = (
                    "já cadastrado",
                    "ja cadastrado",
                    "erro",
                    "inválido",
                    "invalido"
                )

                if any(
                    mensagem in resultado_lower
                    for mensagem in mensagens_erro
                ):

                    QMessageBox.warning(
                        self,
                        "Cadastro",
                        resultado
                    )

                    return

            # --------------------------------------------------
            # Cadastro concluído
            # --------------------------------------------------

            QMessageBox.information(
                self,
                "Cadastro concluído",
                "Conta criada com sucesso! Agora você pode entrar."
            )

            # Limpa os campos
            self.cadastro.input_email_cadastro.clear()
            self.cadastro.input_senha_cadastro.clear()
            self.cadastro.input_confirmacao.clear()

            # Coloca o e-mail automaticamente no login
            self.login.input_email_login.setText(
                email
            )

            self.login.input_senha_login.clear()

            # Volta ao login
            self.abrir_login()

            self.login.input_senha_login.setFocus()

        except Exception as erro:

            print(
                f"Erro ao cadastrar usuário: {erro}"
            )

            QMessageBox.critical(
                self,
                "Erro",
                "Não foi possível realizar o cadastro."
            )

    # ======================================================
    # LOGIN
    # ======================================================

    def realizar_login(self):

        email = (
            self.login
            .input_email_login
            .text()
            .strip()
        )

        senha = (
            self.login
            .input_senha_login
            .text()
        )

        # --------------------------------------------------
        # Campos vazios
        # --------------------------------------------------

        if not email or not senha:

            QMessageBox.warning(
                self,
                "Campos incompletos",
                "Digite seu e-mail e sua senha."
            )

            return

        # --------------------------------------------------
        # Banco de dados
        # --------------------------------------------------

        try:

            resultado = fazer_login(
                email,
                senha
            )

            print(
                f"Resultado do login: {resultado}"
            )

            login_valido = False

            # Caso database.py retorne True
            if resultado is True:

                login_valido = True

            # Caso database.py retorne texto
            elif isinstance(resultado, str):

                resultado_lower = resultado.lower()

                mensagens_sucesso = (
                    "sucesso",
                    "login realizado",
                    "login efetuado"
                )

                if any(
                    mensagem in resultado_lower
                    for mensagem in mensagens_sucesso
                ):

                    login_valido = True

            # --------------------------------------------------
            # Login correto
            # --------------------------------------------------

            if login_valido:

                self.login.input_senha_login.clear()

                self.abrir_dashboard()

                return

            # --------------------------------------------------
            # Login incorreto
            # --------------------------------------------------

            QMessageBox.warning(
                self,
                "Login inválido",
                "E-mail ou senha incorretos."
            )

            self.login.input_senha_login.clear()

            self.login.input_senha_login.setFocus()

        except Exception as erro:

            print(
                f"Erro ao realizar login: {erro}"
            )

            QMessageBox.critical(
                self,
                "Erro",
                "Não foi possível realizar o login."
            )

    # ======================================================
    # LOGOUT
    # ======================================================

    def realizar_logout(self):

        # Limpa qualquer senha deixada na tela
        self.login.input_senha_login.clear()

        # Volta para o login
        self.abrir_login()

        self.login.input_email_login.setFocus()

    # ======================================================
    # ANIMAÇÃO
    # ======================================================

    def animar_pagina(self, pagina):

        efeito = QGraphicsOpacityEffect(
            pagina
        )

        pagina.setGraphicsEffect(
            efeito
        )

        self.animacao_pagina = QPropertyAnimation(
            efeito,
            b"opacity",
            self
        )

        self.animacao_pagina.setDuration(
            260
        )

        self.animacao_pagina.setStartValue(
            0.0
        )

        self.animacao_pagina.setEndValue(
            1.0
        )

        self.animacao_pagina.setEasingCurve(
            QEasingCurve.Type.OutCubic
        )

        self.animacao_pagina.finished.connect(
            lambda: pagina.setGraphicsEffect(None)
        )

        self.animacao_pagina.start()

    # ======================================================
    # ABRIR LOGIN
    # ======================================================

    def abrir_login(self):

        self.pilha.setCurrentWidget(
            self.login
        )

        self.animar_pagina(
            self.login
        )

    # ======================================================
    # ABRIR CADASTRO
    # ======================================================

    def abrir_cadastro(self):

        self.pilha.setCurrentWidget(
            self.cadastro
        )

        self.animar_pagina(
            self.cadastro
        )

    # ======================================================
    # ABRIR DASHBOARD
    # ======================================================

    def abrir_dashboard(self):

        self.pilha.setCurrentWidget(
            self.dashboard
        )

        self.animar_pagina(
            self.dashboard
        )


# ==========================================================
# ESTILO DA APLICAÇÃO
# ==========================================================

STYLE = """

/* ========================================================
   CONFIGURAÇÃO GERAL
======================================================== */

QWidget {
    background-color: #0b0f14;
    color: #f3f5f7;

    font-family:
        "Segoe UI",
        Arial,
        sans-serif;

    font-size: 14px;
}

QLabel {
    background-color: transparent;
}


/* ========================================================
   CARDS DE LOGIN E CADASTRO
======================================================== */

QFrame#authCard {
    background-color: #111720;

    border: 1px solid #202936;

    border-radius: 14px;
}


/* ========================================================
   TÍTULOS
======================================================== */

QLabel#authTitle {
    background-color: transparent;

    color: #f8fafc;

    font-size: 28px;

    font-weight: 700;

    padding: 2px 0px;
}

QLabel#authSubtitle {
    background-color: transparent;

    color: #94a3b8;

    font-size: 13px;

    padding: 0px 4px 6px 4px;
}

QLabel#fieldLabel {
    background-color: transparent;

    color: #cbd5e1;

    font-size: 13px;

    font-weight: 600;

    padding: 2px 0px 0px 0px;
}


/* ========================================================
   INPUTS
======================================================== */

QLineEdit {
    background-color: #0d131b;

    color: #f5f7fa;

    border: 1px solid #263140;

    border-radius: 8px;

    padding: 11px 12px;

    min-height: 20px;

    selection-background-color: #7257ff;
}

QLineEdit:hover {
    border: 1px solid #344255;
}

QLineEdit:focus {
    border: 1px solid #7257ff;

    background-color: #101722;
}

QLineEdit::placeholder {
    color: #5f6b7a;
}


/* ========================================================
   BOTÃO PRINCIPAL
======================================================== */

QPushButton#primaryButton {
    background-color: #7257ff;

    color: white;

    border: none;

    border-radius: 8px;

    padding: 11px 16px;

    font-weight: 600;
}

QPushButton#primaryButton:hover {
    background-color: #826cff;
}

QPushButton#primaryButton:pressed {
    background-color: #6248e8;
}


/* ========================================================
   BOTÃO EM FORMATO DE LINK
======================================================== */

QPushButton#linkButton {
    background-color: transparent;

    color: #8f9bad;

    border: none;

    padding: 8px;
}

QPushButton#linkButton:hover {
    color: #b9c2ce;
}


/* ========================================================
   SIDEBAR
======================================================== */

QFrame#sidebar {
    background-color: #0e141c;

    border-right: 1px solid #202936;
}

QLabel#sidebarLogo {
    color: white;

    font-size: 21px;

    font-weight: 700;
}


/* ========================================================
   MENU
======================================================== */

QPushButton#navButton,
QPushButton#navButtonActive {
    text-align: left;

    border: none;

    border-radius: 7px;

    padding: 11px 12px;

    font-size: 14px;
}

QPushButton#navButton {
    background-color: transparent;

    color: #8491a3;
}

QPushButton#navButton:hover {
    background-color: #151d28;

    color: white;
}

QPushButton#navButtonActive {
    background-color: #1b2330;

    color: white;

    font-weight: 600;
}


/* ========================================================
   SAIR
======================================================== */

QPushButton#logoutButton {
    background-color: transparent;

    color: #7f8b9a;

    border: none;

    text-align: left;

    padding: 10px;
}

QPushButton#logoutButton:hover {
    color: #f3f5f7;
}


/* ========================================================
   DASHBOARD
======================================================== */

QLabel#pageTitle {
    color: white;

    font-size: 28px;

    font-weight: 700;
}

QLabel#pageSubtitle {
    color: #8390a1;

    font-size: 14px;
}

QLabel#sectionTitle {
    color: #f5f7fa;

    font-size: 16px;

    font-weight: 600;
}


/* ========================================================
   CARDS DE ESTATÍSTICA
======================================================== */

QFrame#statCard,
QFrame#contentCard {
    background-color: #111720;

    border: 1px solid #202936;

    border-radius: 10px;
}

QLabel#statTitle {
    color: #8793a4;

    font-size: 13px;
}

QLabel#statValue {
    color: white;

    font-size: 26px;

    font-weight: 700;
}


/* ========================================================
   TABELA
======================================================== */

QTableWidget {
    background-color: #0e141c;

    alternate-background-color: #101720;

    border: 1px solid #202936;

    border-radius: 7px;

    gridline-color: #1c2531;

    selection-background-color: #252f3d;

    selection-color: white;
}

QTableWidget::item {
    padding: 8px;
}

QHeaderView::section {
    background-color: #141b24;

    color: #919dab;

    border: none;

    border-bottom: 1px solid #202936;

    padding: 10px;

    font-weight: 600;
}

"""


# ==========================================================
# INICIAR APLICAÇÃO
# ==========================================================

if __name__ == "__main__":

    app = QApplication(
        sys.argv
    )

    app.setStyleSheet(
        STYLE
    )

    janela = MainWindow()

    janela.show()

    sys.exit(
        app.exec()
    )
