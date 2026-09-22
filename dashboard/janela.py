import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QStackedWidget
)


# ==========================================================
# TELA DE LOGIN
# ==========================================================

class LoginPage(QWidget):

    def __init__(self):
        super().__init__()


        # Layout da tela
        layout = QVBoxLayout()

        # Campo de e-mail
        self.label_email_login = QLabel("E-mail:")
        self.input_email_login = QLineEdit()

        # Campo de senha
        self.label_senha_login = QLabel("Senha:")
        self.input_senha_login = QLineEdit()

        # Botões
        self.botao_login = QPushButton("Login")
        self.botao_cadastro = QPushButton("Cadastre-se")
        layout.addWidget(self.botao_cadastro, alignment=Qt.AlimentFlag.AlingCenter)

        # Adicionando os elementos ao layout
        layout.addWidget(self.label_email_login)
        layout.addWidget(self.input_email_login)

        layout.addWidget(self.label_senha_login)
        layout.addWidget(self.input_senha_login)

        layout.addWidget(self.botao_login)
        layout.addWidget(self.botao_cadastro)

        self.setLayout(layout)


# ==========================================================
# TELA DE CADASTRO
# ==========================================================

class CadastroPage(QWidget):

    def __init__(self):
        super().__init__()

        # Layout da tela
        layout = QVBoxLayout()

        # Campo de e-mail
        self.label_email_cadastro = QLabel("E-mail:")
        self.input_email_cadastro = QLineEdit()

        # Campo de senha
        self.label_senha_cadastro = QLabel("Senha:")
        self.input_senha_cadastro = QLineEdit()

        # Confirmação de senha
        self.label_confirmacao = QLabel("Confirme sua senha:")
        self.input_confirmacao = QLineEdit()

        # Botões
        self.botao_cadastrar = QPushButton("Cadastrar")
        self.botao_voltar = QPushButton("Voltar")

        # Adicionando os elementos ao layout
        layout.addWidget(self.label_email_cadastro)
        layout.addWidget(self.input_email_cadastro)

        layout.addWidget(self.label_senha_cadastro)
        layout.addWidget(self.input_senha_cadastro)

        layout.addWidget(self.label_confirmacao)
        layout.addWidget(self.input_confirmacao)

        layout.addWidget(self.botao_cadastrar)
        layout.addWidget(self.botao_voltar)

        self.setLayout(layout)


# ==========================================================
# TELA DO DASHBOARD
# ==========================================================

class DashboardPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.dashboard_label = QLabel("Dashboard do StatusWatch")

        layout.addWidget(self.dashboard_label)

        self.setLayout(layout)


# ==========================================================
# JANELA PRINCIPAL
# ==========================================================

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("StatusWatch")
        self.resize(1200, 700)
        self.setMinimumSize(1000, 600)

        # Pilha responsável por guardar as páginas
        self.pilha = QStackedWidget()

        # Criando as páginas
        self.login = LoginPage()
        self.cadastro = CadastroPage()
        self.dashboard = DashboardPage()

        # Adicionando as páginas à pilha
        self.pilha.addWidget(self.login)
        self.pilha.addWidget(self.cadastro)
        self.pilha.addWidget(self.dashboard)

        # Colocando a pilha dentro da janela
        self.setCentralWidget(self.pilha)

        # Conectando os botões de navegação
        self.login.botao_cadastro.clicked.connect(
            self.abrir_cadastro
        )

        self.cadastro.botao_voltar.clicked.connect(
            self.abrir_login
        )

    def abrir_login(self):
        self.pilha.setCurrentWidget(self.login)

    def abrir_cadastro(self):
        self.pilha.setCurrentWidget(self.cadastro)

    def abrir_dashboard(self):
        self.pilha.setCurrentWidget(self.dashboard)


# ==========================================================
# INICIAR APLICAÇÃO
# ==========================================================

app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

app.exec()