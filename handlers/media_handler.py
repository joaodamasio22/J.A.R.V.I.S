"""
handlers/media_handler.py — Spotify, YouTube e jogos.
"""

import subprocess
import webbrowser

from handlers.base import BaseHandler
from config import PROGRAMS
from core.logger import log


class MediaHandler(BaseHandler):
    triggers = ["toca", "tocar", "reproduza", "jogar", "youtube"]

    def handle(self, comando: str) -> str | None:
        # ── Música ───────────────────────────────────────────────────────────
        if any(p in comando for p in ["toca", "tocar", "reproduza"]):
            musica = self._extrair_alvo(comando, ["toca", "tocar", "reproduza", "spotify", "youtube"])
            if "spotify" in comando:
                return self._tocar_spotify(musica)
            return self._tocar_youtube(musica)

        # ── Jogos ─────────────────────────────────────────────────────────────
        if "jogar" in comando:
            if any(p in comando for p in ["cs", "counter-strike", "counter strike"]):
                return self._abrir_programa("cs2", "Counter-Strike 2")

        # ── YouTube direto ────────────────────────────────────────────────────
        if "youtube" in comando and not any(p in comando for p in ["toca", "tocar", "reproduza"]):
            webbrowser.open("https://www.youtube.com")
            return "Abrindo YouTube."

        return None

    # ── helpers ───────────────────────────────────────────────────────────────

    def _extrair_alvo(self, comando: str, remover: list[str]) -> str:
        for p in remover:
            comando = comando.replace(p, "")
        return comando.strip()

    def _tocar_youtube(self, musica: str) -> str:
        url = f"https://www.youtube.com/results?search_query={musica.replace(' ', '+')}"
        webbrowser.open(url)
        return f"Tocando {musica} no YouTube."

    def _tocar_spotify(self, musica: str) -> str:
        self._abrir_programa("spotify", "Spotify")
        return f"Abrindo Spotify para tocar {musica}."

    def _abrir_programa(self, chave: str, nome: str) -> str | None:
        caminho = PROGRAMS.get(chave)
        if not caminho:
            log.warning("Programa '%s' não configurado.", chave)
            return f"Caminho do {nome} não configurado."
        try:
            subprocess.Popen([caminho])
            return f"Abrindo {nome}."
        except FileNotFoundError:
            log.error("Executável não encontrado: %s", caminho)
            return f"Não encontrei o {nome}. Verifique o caminho em config.py."
        except Exception as e:
            log.error("Erro ao abrir %s: %s", nome, e)
            return f"Erro ao abrir {nome}."