import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

app = QApplication(sys.argv)

janela = QWidget()
janela.setWindowTitle("Minha Janela")
janela.resize(400, 300)

janela.show()

sys.exit(app.exec_())
