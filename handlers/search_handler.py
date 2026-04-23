"""
handlers/search_handler.py — Pesquisa no Google.
"""

import webbrowser
from handlers.base import BaseHandler


class SearchHandler(BaseHandler):
    triggers = ["pesquise", "pesquisar", "busque", "buscar", "procure", "procurar"]

    def handle(self, comando: str) -> str | None:
        assunto = comando
        for p in self.triggers:
            assunto = assunto.replace(p, "")
        assunto = assunto.strip()

        if not assunto:
            return "O que você quer que eu pesquise?"

        webbrowser.open(f"https://www.google.com/search?q={assunto}")
        return f"Pesquisando sobre {assunto}."