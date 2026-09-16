import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QStackedWidget

app = QApplication(sys.argv)

class main_window(QWidget):
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

        # Adicionar os widgets ao layout de login

        login_layout.addWidget(self.label_usuario)
        login_layout.addWidget(self.input_usuario)
        login_layout.addWidget(self.label_senha)
        login_layout.addWidget(self.input_senha)
        login_layout.addWidget(self.botao_login)


janela = main_window()
janela.show()
app.exec()




        



