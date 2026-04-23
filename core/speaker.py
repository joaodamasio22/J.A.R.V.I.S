"""
core/speaker.py — Speaker com fila de falas e flag "está falando".

Melhorias nesta versão:
- Fila de falas: novas respostas não se perdem enquanto outra toca
- Flag `falando` exposta publicamente: o Listener pode consultá-la
  para ignorar o próprio eco do Jarvis (evita o assistente ouvir a si mesmo)
- Event loop persistente em thread dedicada (mantido da versão anterior)
"""

import asyncio
import os
import queue
import threading

import edge_tts
import pygame

from config import TTS_VOICE, TTS_TEMP_FILE
from core.logger import log


class Speaker:
    """
    Gerencia a fila de falas e a síntese de voz.

    Atributo público:
        falando (threading.Event): setado enquanto o áudio está tocando.
        Consulte antes de processar comandos para evitar auto-eco.
    """

    def __init__(self):
        pygame.mixer.init()

        self.falando = threading.Event()          # ← consultado pelo Brain
        self._fila: queue.Queue[str | None] = queue.Queue()

        self._loop = asyncio.new_event_loop()
        self._loop_thread = threading.Thread(
            target=self._run_loop, daemon=True, name="SpeakerLoop"
        )
        self._loop_thread.start()

        self._worker_thread = threading.Thread(
            target=self._worker, daemon=True, name="SpeakerWorker"
        )
        self._worker_thread.start()

        log.debug("Speaker inicializado.")

    # ── API pública ───────────────────────────────────────────────────────────

    def falar(self, texto: str) -> None:
        """Enfileira texto para fala. Retorna imediatamente (não bloqueia)."""
        if texto and texto.strip():
            self._fila.put(texto)

    def shutdown(self):
        """Para o Speaker de forma limpa."""
        self._fila.put(None)          # sinal de encerramento
        self._worker_thread.join(timeout=5)
        self._loop.call_soon_threadsafe(self._loop.stop)
        self._loop_thread.join(timeout=5)
        pygame.mixer.quit()
        log.debug("Speaker encerrado.")

    # ── internals ─────────────────────────────────────────────────────────────

    def _run_loop(self):
        asyncio.set_event_loop(self._loop)
        self._loop.run_forever()

    def _worker(self):
        """Consome a fila de falas em ordem."""
        while True:
            texto = self._fila.get()
            if texto is None:
                break
            future = asyncio.run_coroutine_threadsafe(
                self._falar_async(texto), self._loop
            )
            try:
                future.result(timeout=30)
            except Exception as e:
                log.error("Erro ao aguardar fala: %s", e)

    async def _falar_async(self, texto: str) -> None:
        arquivo = TTS_TEMP_FILE
        self.falando.set()
        try:
            communicate = edge_tts.Communicate(texto, TTS_VOICE)
            await communicate.save(arquivo)

            pygame.mixer.music.load(arquivo)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                await asyncio.sleep(0.1)

            pygame.mixer.music.unload()
        except Exception as e:
            log.error("Erro no TTS: %s", e)
        finally:
            self.falando.clear()
            if os.path.exists(arquivo):
                try:
                    os.remove(arquivo)
                except OSError:
                    pass