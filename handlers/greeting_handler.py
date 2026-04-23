"""
handlers/greeting_handler.py — Saudações e status do assistente.
"""

from handlers.base import BaseHandler
from config import USER_NAME


class GreetingHandler(BaseHandler):
    triggers = [
        "ta ai", "esta ai", "esta aqui", "ta aqui",
        "bom dia", "boa tarde", "boa noite",
        "tudo certo", "tudo bem", "como vai",
    ]

    def handle(self, comando: str) -> str | None:
        if any(p in comando for p in ["ta ai", "esta ai", "esta aqui", "ta aqui"]):
            return f"Olá {USER_NAME}, estou aqui. O que deseja?"
        if "bom dia" in comando:
            return "Bom dia, chefe. Como você está?"
        if "boa tarde" in comando:
            return "Boa tarde, chefe. Como você está?"
        if "boa noite" in comando:
            return "Boa noite, chefe. Como você está?"
        if any(p in comando for p in ["tudo certo", "tudo bem", "como vai"]):
            return f"Tudo ótimo por aqui, {USER_NAME}. E você?"
        return None