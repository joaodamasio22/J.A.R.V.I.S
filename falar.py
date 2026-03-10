import asyncio
import edge_tts
import pygame
import os

pygame.mixer.init()

async def falar_async(texto):

    voz = "pt-BR-AntonioNeural"
    arquivo = "voz.mp3"

    comunicar = edge_tts.Communicate(texto, voz)
    await comunicar.save(arquivo)

    pygame.mixer.music.load(arquivo)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue

    pygame.mixer.music.unload()
    os.remove(arquivo)


def falar(texto):

    if not texto:
        return

    asyncio.run(falar_async(texto))