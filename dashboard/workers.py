"""Executa I/O fora da interface; os sinais retornam à thread da janela."""

from PySide6.QtCore import QThread, Signal


class Task(QThread):
    success = Signal(object)
    failure = Signal(str)

    def __init__(self, operation, parent=None):
        super().__init__(parent)
        self.operation = operation

    def run(self):
        try:
            self.success.emit(self.operation())
        except ValueError as error:
            self.failure.emit(str(error))
        except Exception:
            # Erros do driver podem conter host/credenciais: não exibimos o texto bruto.
            self.failure.emit(
                "Não foi possível concluir. Confira a conexão, o .env e a migração do banco (sql/001_atualizar.sql)."
            )
