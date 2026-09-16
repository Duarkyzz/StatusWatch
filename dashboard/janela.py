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

        # Configurar o layout do widget de login

        login_layout = QVBoxLayout()
        self.label_usuario = QLabel("Usuário:")
        self.input_usuario = QLineEdit()

        self.label_senha = QLabel("Senha:")
        self.input_senha = QLineEdit()

        self.botao_login = QPushButton("Login")

        # Conectar o sinal clicked na função

        self.botao_login.clicked.connect(self.botao_clicado)

        # Adicionar os widgets ao layout de login

        login_layout.addWidget(self.label_usuario)
        login_layout.addWidget(self.input_usuario)
        login_layout.addWidget(self.label_senha)
        login_layout.addWidget(self.input_senha)
        login_layout.addWidget(self.botao_login)

        self.login.setLayout(login_layout)
        self.pilha.addWidget(self.login)
        self.setCentralWidget(self.pilha)

        # Configurar o layout de widget do dashboard

        dashboard_layout = QVBoxLayout()
        self.dashboard_label = QLabel("Dashboard do StatusWatch")

        dashboard_layout.addWidget(self.dashboard_label)

        self.dashboard.setLayout(dashboard_layout)
        self.pilha.addWidget(self.dashboard)

        # Função do botão

    def botao_clicado(self):
        usuario = self.input_usuario.text()
        print(usuario)
        senha = self.input_senha.text()
        print(senha)


janela = main_window()
janela.show()
app.exec()
