"""
services/ai_service.py — Integração com OpenRouter / OpenAI.

Isolado aqui para que trocar de modelo ou provider
não exija mexer em nenhum outro arquivo.
"""

import time
from datetime import datetime

from openai import OpenAI

from config import (
    AI_API_KEY,
    AI_BASE_URL,
    AI_MODEL,
    AI_MAX_TOKENS,
    AI_RETRIES,
    AI_RETRY_WAIT,
    AI_SYSTEM_PROMPT,
    ASSISTANT_NAME,
    USER_NAME,
)
from core.logger import log


class AIService:
    def __init__(self):
        self._client = OpenAI(api_key=AI_API_KEY, base_url=AI_BASE_URL)
        log.debug("AIService inicializado. Modelo: %s", AI_MODEL)

    def perguntar(self, pergunta: str) -> str:
        agora = datetime.now()
        system = AI_SYSTEM_PROMPT.format(
            assistant=ASSISTANT_NAME,
            user=USER_NAME,
            datetime=agora.strftime("%A, %d de %B de %Y, %H:%M"),
        )

        for tentativa in range(1, AI_RETRIES + 1):
            try:
                resposta = self._client.chat.completions.create(
                    model=AI_MODEL,
                    max_tokens=AI_MAX_TOKENS,
                    messages=[
                        {"role": "system", "content": system},
                        {"role": "user",   "content": pergunta},
                    ],
                )
                return resposta.choices[0].message.content
            except Exception as e:
                log.warning("IA tentativa %d/%d falhou: %s", tentativa, AI_RETRIES, e)
                if tentativa < AI_RETRIES:
                    time.sleep(AI_RETRY_WAIT)

        return f"Desculpe, {USER_NAME}, estou com problemas no momento."