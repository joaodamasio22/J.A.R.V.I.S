"""
handlers/datetime_handler.py — Responde perguntas de data e hora.
"""

from datetime import datetime
from handlers.base import BaseHandler
from config import USER_NAME


class DateTimeHandler(BaseHandler):
    triggers = ["que dia", "que horas", "hora certa", "data", "horas sao"]

    def handle(self, comando: str) -> str | None:
        agora = datetime.now()
        if "hora" in comando:
            return f"São {agora.strftime('%H:%M')}, {USER_NAME}."
        return f"Hoje é {agora.strftime('%d/%m/%Y')}, {agora.strftime('%A')}."