import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QStackedWidget

app = QApplication(sys.argv)

class main_window(QMainWindow):
    def __init__(self):

        super().__init__()

        # Criar a pilha de widgets
        self.pilha = QStackedWidget()

        # Criar os widgets de login e dashboard
        self.login = QWidget()
        self.dashboard = QWidget()
        self.cadastro = QWidget()

        # Configurar o layout do widget de login

        login_layout = QVBoxLayout()
        self.label_email_login = QLabel("E-mail:")
        self.input_email_login = QLineEdit()

        self.label_senha_login = QLabel("Senha:")
        self.input_senha_login = QLineEdit()

        self.botao_login = QPushButton("Login")
        self.botao_cadastro = QPushButton("Cadastre")

        # Conectar o sinal clicked na função

        self.botao_cadastro.clicked.connect(self.cadastro)

        # Adicionar os widgets ao layout de login

        login_layout.addWidget(self.label_email_login)
        login_layout.addWidget(self.input_email_login)
        login_layout.addWidget(self.label_senha_login)
        login_layout.addWidget(self.input_senha_login)
        login_layout.addWidget(self.botao_login)
        login_layout.addWidget(self.botao_cadastro)

        self.login.setLayout(login_layout)
        self.pilha.addWidget(self.login)
        self.setCentralWidget(self.pilha)

        # Configurar o layout de widget do dashboard

        dashboard_layout = QVBoxLayout()
        self.dashboard_label = QLabel("Dashboard do StatusWatch")

        # Configurar o layout de widget do dashboard

        dashboard_layout.addWidget(self.dashboard_label)

        self.dashboard.setLayout(dashboard_layout)
        self.pilha.addWidget(self.dashboard)

        # Configurar o layout de widget do cadastro

        cadastro_layout = QVBoxLayout()
        self.label_email_cadastro = QLabel ("E-mail: ")
        self.input_email_cadastro = QLineEdit()

        self.label_senha_cadastro = QLabel ("Senha: ")
        self.input_senha_cadastro  = QLineEdit()

        self.label_confirmacao = QLabel ("Confirme sua senha: ")
        self.input_confirmacao = QLineEdit()

        self.botao_voltar = QPushButton("Voltar")
        self.botao_voltar.clicked.connect(self.login)

        # Adicionar os widgets ao layout do cadastro

        cadastro_layout.addWidget(self.label_email_cadastro)
        cadastro_layout.addWidget(self.input_email_cadastro)
        cadastro_layout.addWidget(self.label_senha_cadastro)
        cadastro_layout.addWidget(self.input_senha_cadastro)
        cadastro_layout.addWidget(self.label_confirmacao)
        cadastro_layout.addWidget(self.input_confirmacao)

        self.cadastro.setLayout(cadastro_layout)
        self.pilha.addWidget(self.cadastro)



janela = main_window()
janela.show()
app.exec()
