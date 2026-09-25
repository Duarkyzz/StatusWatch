from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
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
)


class LoginPage(QWidget):
    def __init__(self):
        super().__init__()

        layout_principal = QVBoxLayout(self)

        layout_principal.setContentsMargins(40, 40, 40, 40)

        layout_principal.addStretch()

        self.card_login = QFrame()

        self.card_login.setObjectName("authCard")

        self.card_login.setFixedWidth(420)

        layout_card = QVBoxLayout(self.card_login)

        layout_card.setContentsMargins(36, 36, 36, 36)

        layout_card.setSpacing(14)

        self.titulo = QLabel("StatusWatch")

        self.titulo.setObjectName("authTitle")

        self.titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.subtitulo = QLabel("Monitore seus sites e serviços em um só lugar.")

        self.subtitulo.setObjectName("authSubtitle")

        self.subtitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.subtitulo.setWordWrap(True)

        self.label_email_login = QLabel("E-mail")

        self.label_email_login.setObjectName("fieldLabel")

        self.input_email_login = QLineEdit()

        self.input_email_login.setPlaceholderText("seuemail@exemplo.com")

        self.label_senha_login = QLabel("Senha")

        self.label_senha_login.setObjectName("fieldLabel")

        self.input_senha_login = QLineEdit()

        self.input_senha_login.setPlaceholderText("Digite sua senha")

        self.input_senha_login.setEchoMode(QLineEdit.EchoMode.Password)

        self.botao_login = QPushButton("Entrar")

        self.botao_login.setObjectName("primaryButton")

        self.botao_login.setCursor(Qt.CursorShape.PointingHandCursor)

        self.botao_cadastro = QPushButton("Criar uma conta")

        self.botao_cadastro.setObjectName("linkButton")

        self.botao_cadastro.setCursor(Qt.CursorShape.PointingHandCursor)

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
            self.card_login, alignment=Qt.AlignmentFlag.AlignCenter
        )

        layout_principal.addStretch()


# ==========================================================
# TELA DE CADASTRO
# ==========================================================


class CadastroPage(QWidget):
    def __init__(self):
        super().__init__()

        layout_principal = QVBoxLayout(self)

        layout_principal.setContentsMargins(40, 40, 40, 40)

        layout_principal.addStretch()

        self.card_cadastro = QFrame()

        self.card_cadastro.setObjectName("authCard")

        self.card_cadastro.setFixedWidth(420)

        layout_card = QVBoxLayout(self.card_cadastro)

        layout_card.setContentsMargins(36, 36, 36, 36)

        layout_card.setSpacing(14)

        self.titulo = QLabel("Criar conta")

        self.titulo.setObjectName("authTitle")

        self.titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.subtitulo = QLabel(
            "Crie sua conta para começar a monitorar seus serviços."
        )

        self.subtitulo.setObjectName("authSubtitle")

        self.subtitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.subtitulo.setWordWrap(True)

        self.label_email_cadastro = QLabel("E-mail")

        self.label_email_cadastro.setObjectName("fieldLabel")

        self.input_email_cadastro = QLineEdit()

        self.input_email_cadastro.setPlaceholderText("seuemail@exemplo.com")

        self.label_senha_cadastro = QLabel("Senha")

        self.label_senha_cadastro.setObjectName("fieldLabel")

        self.input_senha_cadastro = QLineEdit()

        self.input_senha_cadastro.setPlaceholderText("Digite sua senha")

        self.input_senha_cadastro.setEchoMode(QLineEdit.EchoMode.Password)

        self.label_confirmacao = QLabel("Confirme sua senha")

        self.label_confirmacao.setObjectName("fieldLabel")

        self.input_confirmacao = QLineEdit()

        self.input_confirmacao.setPlaceholderText("Digite sua senha novamente")

        self.input_confirmacao.setEchoMode(QLineEdit.EchoMode.Password)

        self.botao_cadastrar = QPushButton("Cadastrar")

        self.botao_cadastrar.setObjectName("primaryButton")

        self.botao_cadastrar.setCursor(Qt.CursorShape.PointingHandCursor)

        self.botao_voltar = QPushButton("Voltar para o login")

        self.botao_voltar.setObjectName("linkButton")

        self.botao_voltar.setCursor(Qt.CursorShape.PointingHandCursor)

        layout_card.addWidget(self.titulo)

        layout_card.addWidget(self.subtitulo)

        layout_card.addSpacing(14)

        layout_card.addWidget(self.label_email_cadastro)

        layout_card.addWidget(self.input_email_cadastro)

        layout_card.addWidget(self.label_senha_cadastro)

        layout_card.addWidget(self.input_senha_cadastro)

        layout_card.addWidget(self.label_confirmacao)

        layout_card.addWidget(self.input_confirmacao)

        layout_card.addSpacing(8)

        layout_card.addWidget(self.botao_cadastrar)

        layout_card.addWidget(self.botao_voltar)

        layout_principal.addWidget(
            self.card_cadastro, alignment=Qt.AlignmentFlag.AlignCenter
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

        layout.setContentsMargins(22, 18, 22, 18)

        layout.setSpacing(4)

        self.label_titulo = QLabel(titulo)

        self.label_titulo.setObjectName("statTitle")

        self.label_valor = QLabel(valor)

        self.label_valor.setObjectName("statValue")

        layout.addWidget(self.label_titulo)

        layout.addWidget(self.label_valor)


# ==========================================================
# DASHBOARD
# ==========================================================


class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()

        layout_principal = QHBoxLayout(self)

        layout_principal.setContentsMargins(0, 0, 0, 0)

        layout_principal.setSpacing(0)

        # ==================================================
        # SIDEBAR
        # ==================================================

        self.sidebar = QFrame()

        self.sidebar.setObjectName("sidebar")

        self.sidebar.setFixedWidth(220)

        sidebar_layout = QVBoxLayout(self.sidebar)

        sidebar_layout.setContentsMargins(22, 28, 22, 28)

        sidebar_layout.setSpacing(10)

        self.logo = QLabel("StatusWatch")

        self.logo.setObjectName("sidebarLogo")

        sidebar_layout.addWidget(self.logo)

        sidebar_layout.addSpacing(30)

        self.menu_dashboard = QPushButton("Dashboard")

        self.menu_dashboard.setObjectName("navButtonActive")

        self.menu_dashboard.setCursor(Qt.CursorShape.PointingHandCursor)

        self.menu_historico = QPushButton("Histórico")

        self.menu_historico.setObjectName("navButton")

        self.menu_historico.setCursor(Qt.CursorShape.PointingHandCursor)

        sidebar_layout.addWidget(self.menu_dashboard)

        sidebar_layout.addWidget(self.menu_historico)

        sidebar_layout.addStretch()

        self.botao_sair = QPushButton("Sair")

        self.botao_sair.setObjectName("logoutButton")

        self.botao_sair.setCursor(Qt.CursorShape.PointingHandCursor)

        sidebar_layout.addWidget(self.botao_sair)

        # ==================================================
        # ÁREA CENTRAL
        # ==================================================

        self.paginas = QStackedWidget()

        # ==================================================
        # PÁGINA PRINCIPAL DO DASHBOARD
        # ==================================================

        self.pagina_dashboard = QWidget()

        conteudo_layout = QVBoxLayout(self.pagina_dashboard)

        conteudo_layout.setContentsMargins(34, 30, 34, 30)

        conteudo_layout.setSpacing(22)

        self.dashboard_titulo = QLabel("Dashboard")

        self.dashboard_titulo.setObjectName("pageTitle")

        self.dashboard_subtitulo = QLabel("Acompanhe o status dos seus serviços.")

        self.dashboard_subtitulo.setObjectName("pageSubtitle")

        conteudo_layout.addWidget(self.dashboard_titulo)

        conteudo_layout.addWidget(self.dashboard_subtitulo)

        # ==================================================
        # ESTATÍSTICAS
        # ==================================================

        stats_layout = QHBoxLayout()

        stats_layout.setSpacing(16)

        self.card_monitorados = StatCard("Monitorados", "0")

        self.card_online = StatCard("Online", "0")

        self.card_offline = StatCard("Offline", "0")

        stats_layout.addWidget(self.card_monitorados)

        stats_layout.addWidget(self.card_online)

        stats_layout.addWidget(self.card_offline)

        conteudo_layout.addLayout(stats_layout)

        # ==================================================
        # ADICIONAR MONITOR
        # ==================================================

        self.monitor_card = QFrame()

        self.monitor_card.setObjectName("contentCard")

        monitor_layout = QVBoxLayout(self.monitor_card)

        monitor_layout.setContentsMargins(22, 20, 22, 20)

        monitor_layout.setSpacing(12)

        self.monitor_titulo = QLabel("Adicionar monitor")

        self.monitor_titulo.setObjectName("sectionTitle")

        monitor_layout.addWidget(self.monitor_titulo)

        url_layout = QHBoxLayout()

        url_layout.setSpacing(10)

        self.input_url = QLineEdit()

        self.input_url.setPlaceholderText("https://exemplo.com")

        self.botao_adicionar = QPushButton("Adicionar")

        self.botao_adicionar.setObjectName("primaryButton")

        self.botao_adicionar.setFixedWidth(130)

        self.botao_adicionar.setCursor(Qt.CursorShape.PointingHandCursor)

        url_layout.addWidget(self.input_url)

        url_layout.addWidget(self.botao_adicionar)

        monitor_layout.addLayout(url_layout)

        conteudo_layout.addWidget(self.monitor_card)

        # ==================================================
        # TABELA PRINCIPAL
        # ==================================================

        self.servicos_card = QFrame()

        self.servicos_card.setObjectName("contentCard")

        servicos_layout = QVBoxLayout(self.servicos_card)

        servicos_layout.setContentsMargins(22, 20, 22, 20)

        servicos_layout.setSpacing(14)

        self.servicos_titulo = QLabel("Últimas verificações")

        self.servicos_titulo.setObjectName("sectionTitle")

        servicos_layout.addWidget(self.servicos_titulo)

        self.tabela_servicos = self.criar_tabela()

        servicos_layout.addWidget(self.tabela_servicos)

        conteudo_layout.addWidget(self.servicos_card)

        # ==================================================
        # PÁGINA HISTÓRICO
        # ==================================================

        self.pagina_historico = QWidget()

        historico_layout = QVBoxLayout(self.pagina_historico)

        historico_layout.setContentsMargins(34, 30, 34, 30)

        historico_layout.setSpacing(22)

        self.historico_titulo = QLabel("Histórico")

        self.historico_titulo.setObjectName("pageTitle")

        self.historico_subtitulo = QLabel("Consulte todas as verificações realizadas.")

        self.historico_subtitulo.setObjectName("pageSubtitle")

        historico_layout.addWidget(self.historico_titulo)

        historico_layout.addWidget(self.historico_subtitulo)

        self.historico_card = QFrame()

        self.historico_card.setObjectName("contentCard")

        historico_card_layout = QVBoxLayout(self.historico_card)

        historico_card_layout.setContentsMargins(22, 20, 22, 20)

        self.tabela_historico = self.criar_tabela()

        historico_card_layout.addWidget(self.tabela_historico)

        historico_layout.addWidget(self.historico_card)

        # ==================================================
        # ADICIONAR PÁGINAS
        # ==================================================

        self.paginas.addWidget(self.pagina_dashboard)

        self.paginas.addWidget(self.pagina_historico)

        layout_principal.addWidget(self.sidebar)

        layout_principal.addWidget(self.paginas)

        # ==================================================
        # NAVEGAÇÃO INTERNA
        # ==================================================

        self.menu_dashboard.clicked.connect(self.abrir_dashboard)

        self.menu_historico.clicked.connect(self.abrir_historico)

    def criar_tabela(self):

        tabela = QTableWidget()

        tabela.setColumnCount(5)

        tabela.setHorizontalHeaderLabels(["URL", "Status", "HTTP", "Resposta", "Data"])

        tabela.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        tabela.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        tabela.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        tabela.verticalHeader().setVisible(False)

        tabela.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        tabela.setAlternatingRowColors(True)

        return tabela

    def abrir_dashboard(self):

        self.paginas.setCurrentWidget(self.pagina_dashboard)

        self.menu_dashboard.setObjectName("navButtonActive")

        self.menu_historico.setObjectName("navButton")

        self.atualizar_estilo_menu()

    def abrir_historico(self):

        self.paginas.setCurrentWidget(self.pagina_historico)

        self.menu_dashboard.setObjectName("navButton")

        self.menu_historico.setObjectName("navButtonActive")

        self.atualizar_estilo_menu()

    def atualizar_estilo_menu(self):

        for botao in (self.menu_dashboard, self.menu_historico):
            botao.style().unpolish(botao)

            botao.style().polish(botao)
