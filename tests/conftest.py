import os

os.environ["QT_QPA_PLATFORM"] = "offscreen"
os.environ["DATABASE_URL"] = "postgresql://test:test@127.0.0.1:1/test"
import pytest
from PySide6.QtWidgets import QApplication


@pytest.fixture(scope="session")
def qtapp():
    app = QApplication.instance() or QApplication([])
    yield app
