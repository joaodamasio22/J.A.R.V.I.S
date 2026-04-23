"""
handlers/system_handler.py — Abre programas e arquivos do sistema.
"""

import subprocess
import os

from handlers.base import BaseHandler
from config import PROGRAMS, FILE_SEARCH_PATHS
from core.logger import log


class SystemHandler(BaseHandler):
    triggers = ["abrir", "abre", "iniciar", "inicia"]

    def handle(self, comando: str) -> str | None:
        # Remove o gatilho para isolar o alvo
        alvo = comando
        for p in self.triggers:
            alvo = alvo.replace(p, "")
        alvo = alvo.strip()

        if not alvo:
            return "O que você quer que eu abra?"

        # 1. Verifica programas conhecidos primeiro (mais rápido)
        for nome, caminho in PROGRAMS.items():
            if nome in alvo:
                return self._executar(caminho, nome)

        # 2. Busca no sistema de arquivos
        caminho = self._procurar_arquivo(alvo)
        if caminho:
            return self._executar(caminho, alvo)

        return f"Não encontrei '{alvo}'. Verifique se está configurado em config.py."

    def _executar(self, caminho: str, nome: str) -> str:
        try:
            if caminho.lower().endswith(".exe"):
                subprocess.Popen([caminho])
            else:
                os.startfile(caminho)
            return f"Abrindo {nome}."
        except FileNotFoundError:
            log.error("Arquivo não encontrado: %s", caminho)
            return f"Não encontrei o arquivo de {nome}."
        except Exception as e:
            log.error("Erro ao abrir %s: %s", nome, e)
            return f"Erro ao abrir {nome}."

    def _procurar_arquivo(self, nome: str) -> str | None:
        log.debug("Procurando arquivo: %s", nome)
        for pasta in FILE_SEARCH_PATHS:
            for root, _, files in os.walk(pasta):
                for file in files:
                    if nome.lower() in file.lower():
                        return os.path.join(root, file)
        return None