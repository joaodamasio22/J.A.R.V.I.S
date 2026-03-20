import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

from ouvir import ouvir
from falar import falar

from comandos import perguntar_ia, comandos_personalizados
from system import (
    executar_comandos,
    abrir_youtube,
    tocar_spotify,
    tocar_youtube,
    iniciar_cs,
    abrir_arquivo_ou_programa
)
from pesquisa import pesquisar

import unidecode  
import time


while True:
    comando = ouvir()
    if not comando:
        time.sleep(0.3)
        continue

    comando = unidecode.unidecode(comando.lower().strip())
    comando = comando.replace("jarvis", "").strip()

    resposta = None

    # --- COMANDOS DE MÚSICA ---
    if "toca" in comando or "tocar" in comando or "reproduza" in comando:
        musica = comando.replace("toca", "").replace("tocar", "").replace("reproduza", "").replace("spotify", "").strip()
        
        if "spotify" in comando:
            resposta = tocar_spotify(musica)
        else:
            resposta = tocar_youtube(musica)
        
        if resposta:
            falar(resposta)
            continue

    # --- COMANDO JOGAR CS2 ---
    if "jogar" in comando:
        resposta = iniciar_cs(comando)
        if resposta:
            falar(resposta)
        continue

    # --- ABRIR ARQUIVOS OU PROGRAMAS ---
    if "abrir" in comando:
        nome_arquivo = comando.replace("abrir", "").strip()
        resposta = abrir_arquivo_ou_programa(nome_arquivo)
        falar(resposta)
        continue

    # --- COMANDOS PERSONALIZADOS ---
    resposta = comandos_personalizados(comando)

    # --- EXECUTAR PROGRAMAS DO PC ---
    if not resposta:
        resposta = executar_comandos(comando)

    # --- ABRIR YOUTUBE ---
    if not resposta:
        resposta = abrir_youtube(comando)

    # --- PESQUISAR ---
    if not resposta and "pesquisar" in comando:
        resposta = pesquisar(comando)

    # --- SAIR ---
    if not resposta and "sair" in comando:
        falar("Até mais! finalizando sistemas...")
        break

    # --- CONSULTAR IA ---
    if not resposta:
        resposta = perguntar_ia(comando)

    # --- FALAR RESPOSTA ---
    if resposta:
        falar(resposta)