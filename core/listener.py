"""
core/listener.py — Listener com thread dedicada e fila de comandos.

Problema resolvido: o Listener original bloqueava o loop principal.
Durante o recognize_google() (chamada de rede), o programa ficava parado.

Solução: Listener roda em thread própria e coloca comandos numa Queue.
O loop principal consome a fila sem bloquear.

Fluxo:
    Thread Listener → queue_comandos → Thread Brain
"""

import queue
import threading
import speech_recognition as sr

from config import (
    STT_LANGUAGE,
    STT_ENERGY_THRESHOLD,
    STT_PAUSE_THRESHOLD,
    STT_PHRASE_THRESHOLD,
    STT_NON_SPEAKING,
    STT_LISTEN_TIMEOUT,
    STT_PHRASE_LIMIT,
    STT_AMBIENT_DURATION,
)
from core.logger import log


class Listener:
    """
    Captura voz continuamente em background e disponibiliza
    comandos via fila thread-safe.
    """

    def __init__(self, comando_queue: queue.Queue):
        self._queue = comando_queue
        self._parado = threading.Event()

        self._recognizer = sr.Recognizer()
        self._recognizer.energy_threshold      = STT_ENERGY_THRESHOLD
        self._recognizer.pause_threshold       = STT_PAUSE_THRESHOLD
        self._recognizer.phrase_threshold      = STT_PHRASE_THRESHOLD
        self._recognizer.non_speaking_duration = STT_NON_SPEAKING

        self._thread = threading.Thread(target=self._loop, daemon=True, name="Listener")
        log.debug("Listener criado.")

    def iniciar(self):
        self._thread.start()
        log.info("Listener iniciado em background.")

    def parar(self):
        self._parado.set()
        log.debug("Listener sinalizado para parar.")

    # ── loop interno (roda em thread própria) ─────────────────────────────────

    def _loop(self):
        while not self._parado.is_set():
            texto = self._capturar()
            if texto:
                self._queue.put(texto)

    def _capturar(self) -> str | None:
        try:
            with sr.Microphone() as source:
                self._recognizer.adjust_for_ambient_noise(
                    source, duration=STT_AMBIENT_DURATION
                )
                log.debug("Ouvindo…")
                audio = self._recognizer.listen(
                    source,
                    timeout=STT_LISTEN_TIMEOUT,
                    phrase_time_limit=STT_PHRASE_LIMIT,
                )
        except sr.WaitTimeoutError:
            return None
        except Exception as e:
            log.error("Erro ao capturar áudio: %s", e)
            return None

        try:
            texto = self._recognizer.recognize_google(audio, language=STT_LANGUAGE)
            log.info("Entendido: '%s'", texto)
            return texto.lower()
        except sr.UnknownValueError:
            log.debug("Áudio não reconhecido.")
            return None
        except sr.RequestError as e:
            log.error("Erro no serviço STT: %s", e)
            return None