import unidecode
 
from handlers.base import BaseHandler
from handlers.datetime_handler import DateTimeHandler
from handlers.greeting_handler import GreetingHandler
from handlers.media_handler import MediaHandler
from handlers.system_handler import SystemHandler
from handlers.search_handler import SearchHandler
from services.ai_service import AIService
from core.logger import log
from config import ASSISTANT_NAME
 
 
class Brain:
    """
    Recebe um comando em texto e retorna a resposta adequada.
    Percorre os handlers em ordem; o primeiro que aceitar o comando vence.
    Se nenhum aceitar, delega à IA.
    """
 
    def __init__(self):
        self._handlers: list[BaseHandler] = [
            GreetingHandler(),
            DateTimeHandler(),
            MediaHandler(),
            SearchHandler(),
            SystemHandler(),   # ← SystemHandler por último: trigger "abrir" é genérico
        ]
        self._ai = AIService()
        log.info("Brain inicializado com %d handlers.", len(self._handlers))
 
    def processar(self, texto_bruto: str) -> str | None:
        # Normalização: remove acentos, lower, remove nome do assistente
        comando = unidecode.unidecode(texto_bruto).lower().strip()
        comando = comando.replace(ASSISTANT_NAME.lower(), "").strip()
        log.debug("Comando normalizado: '%s'", comando)
 
        if not comando:
            return None
 
        # Palavra de saída
        if "sair" in comando:
            return "__EXIT__"
 
        # Percorre handlers
        for handler in self._handlers:
            if handler.can_handle(comando):
                log.info("Handler: %s", type(handler).__name__)
                resposta = handler.handle(comando)
                if resposta:
                    return resposta
 
        # Fallback: IA
        log.info("Delegando à IA.")
        return self._ai.perguntar(comando)
 