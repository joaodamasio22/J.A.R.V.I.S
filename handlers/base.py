"""
handlers/base.py — Contrato base para todos os handlers de comando.

COMO ADICIONAR UM NOVO COMANDO:
1. Crie um arquivo em handlers/, ex: handlers/weather_handler.py
2. Herde de BaseHandler
3. Defina `triggers` com as palavras que ativam o handler
4. Implemente o método `handle(comando)`
5. Registre no brain.py (uma linha só)

Pronto. Sem mexer em nada mais.
"""

from abc import ABC, abstractmethod


class BaseHandler(ABC):
    """
    Classe base para handlers de comando.

    Cada subclasse declara quais palavras-chave a ativam (triggers)
    e implementa a lógica em handle().
    """

    # Palavras-chave que ativam este handler.
    # Ex: triggers = ["toca", "tocar", "reproduza"]
    triggers: list[str] = []

    def can_handle(self, comando: str) -> bool:
        """Retorna True se algum trigger estiver presente no comando."""
        return any(t in comando for t in self.triggers)

    @abstractmethod
    def handle(self, comando: str) -> str | None:
        """
        Processa o comando e retorna a resposta em texto,
        ou None se não souber responder.
        """
        ...