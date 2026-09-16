import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit

app = QApplication(sys.argv)

janela = QWidget()
janela.setWindowTitle("StatusWatch")
janela.resize(800, 700)

layoyut = QVBoxLayout()

titulo = QLabel("StatusWatch")
titulo.setStyleSheet("font-size: 24px; font-weight: bold;")

campo_url = QLineEdit()
campo_url.setPlaceholderText("Digite a URL do site")

botao_verificar = QPushButton("Verificar Status")

layoyut.addWidget(titulo)
layoyut.addWidget(campo_url)
layoyut.addWidget(botao_verificar)

janela.setLayout(layoyut)

janela.show()

app.exec()
