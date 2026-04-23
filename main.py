"""
main.py — Ponto de entrada do Jarvis.

Pipeline assíncrono com 3 workers paralelos:

    ┌─────────────┐    queue_comandos    ┌──────────────┐    queue_respostas    ┌─────────────┐
    │  Listener   │ ──────────────────► │    Brain     │ ──────────────────► │   Speaker   │
    │  (Thread)   │                     │   (Thread)   │                     │  (Thread)   │
    └─────────────┘                     └──────────────┘                     └─────────────┘

- Listener nunca para de ouvir, nem durante respostas
- Brain processa comandos sem esperar o áudio terminar
- Speaker enfileira falas e toca em sequência
- flag speaker.falando evita que o Jarvis ouça o próprio eco
"""

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

import queue
import threading
import time

from core.listener import Listener
from core.speaker  import Speaker
from core.brain    import Brain
from core.logger   import log
from config        import ASSISTANT_NAME, USER_NAME

SENTINEL = "__EXIT__"


def brain_worker(
    cmd_queue: queue.Queue,
    resp_queue: queue.Queue,
    speaker: Speaker,
    brain: Brain,
    stop_event: threading.Event,
):
    log.info("Brain worker iniciado.")
    while not stop_event.is_set():
        try:
            texto = cmd_queue.get(timeout=0.5)
        except queue.Empty:
            continue

        if speaker.falando.is_set():
            log.debug("Eco ignorado: '%s'", texto)
            continue

        log.info("Processando: '%s'", texto)
        resposta = brain.processar(texto)

        if resposta == SENTINEL:
            resp_queue.put(SENTINEL)
            stop_event.set()
            break

        if resposta:
            resp_queue.put(resposta)

    log.info("Brain worker encerrado.")


def speaker_worker(
    resp_queue: queue.Queue,
    speaker: Speaker,
    stop_event: threading.Event,
):
    """Consome respostas e envia ao Speaker."""
    log.info("Speaker worker iniciado.")
    while not stop_event.is_set():
        try:
            texto = resp_queue.get(timeout=0.5)
        except queue.Empty:
            continue

        if texto == SENTINEL:
            break

        speaker.falar(texto)

    log.info("Speaker worker encerrado.")


def main():
    log.info("Iniciando %s para %s…", ASSISTANT_NAME, USER_NAME)

    cmd_queue:  queue.Queue[str] = queue.Queue()
    resp_queue: queue.Queue[str] = queue.Queue()
    stop_event = threading.Event()

    speaker = Speaker()
    brain   = Brain()
    listener = Listener(cmd_queue)

    # Inicia os workers
    t_brain = threading.Thread(
        target=brain_worker,
        args=(cmd_queue, resp_queue, speaker, brain, stop_event),
        daemon=True,
        name="BrainWorker",
    )
    t_speaker = threading.Thread(
        target=speaker_worker,
        args=(resp_queue, speaker, stop_event),
        daemon=True,
        name="SpeakerWorker",
    )

    t_brain.start()
    t_speaker.start()
    listener.iniciar()

    speaker.falar(f"Sistema online. Olá, {USER_NAME}.")

    try:
        # Loop principal só monitora o stop_event
        while not stop_event.is_set():
            time.sleep(0.2)
    except KeyboardInterrupt:
        log.info("Interrompido pelo usuário.")
        stop_event.set()
    finally:
        listener.parar()
        t_brain.join(timeout=3)
        t_speaker.join(timeout=3)
        speaker.shutdown()
        log.info("%s encerrado.", ASSISTANT_NAME)


if __name__ == "__main__":
    main()