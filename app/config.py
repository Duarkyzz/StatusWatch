"""Configuração funciona pelo código e pelo executável, sem depender do terminal."""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = (
    Path(sys.executable).parent
    if getattr(sys, "frozen", False)
    else Path(__file__).resolve().parents[1]
)


def database_url():
    load_dotenv(BASE_DIR / ".env", override=False)
    url = os.getenv("DATABASE_URL", "").strip()
    if not url:
        raise ValueError(
            "Configure DATABASE_URL no arquivo .env ao lado do programa e tente novamente."
        )
    return url
