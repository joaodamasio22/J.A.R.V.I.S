import asyncio
import edge_tts
import pygame
import os

pygame.mixer.init()

async def falar_async(texto):
    voz = "pt-BR-AntonioNeural"
    arquivo = "voz.mp3"

    try:
        comunicar = edge_tts.Communicate(texto, voz)
        await comunicar.save(arquivo)

        pygame.mixer.music.load(arquivo)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            await asyncio.sleep(0.1) 

        pygame.mixer.music.unload()
        os.remove(arquivo)
    except Exception as e:
        print(f"Erro no audio: {e}")

def falar(texto):
    if not texto:
        return
    try:
        asyncio.run(falar_async(texto)) 
    except Exception as e:
        print(f"Erro ao falar: {e}")