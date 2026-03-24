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
    print(f"🔍 Comando processado: '{comando}'") 
    resposta = None

    if "sair" in comando:
        falar("Ate mais! finalizando sistemas...")
        break

    if any(p in comando for p in ["toca", "tocar", "reproduza"]):
        musica = comando
        for p in ["toca", "tocar", "reproduza", "spotify"]:
            musica = musica.replace(p, "")
        musica = musica.strip()
        if "spotify" in comando:
            resposta = tocar_spotify(musica)
        else:
            resposta = tocar_youtube(musica)
        if resposta:
            falar(resposta)
        continue

    if "jogar" in comando:
        resposta = iniciar_cs(comando)
        if resposta:
            falar(resposta)
        continue

    if "abrir" in comando:
        nome_arquivo = comando.replace("abrir", "").strip()
        resposta = abrir_arquivo_ou_programa(nome_arquivo)
        falar(resposta)
        continue

    palavras_pesquisa = ["pesquise", "pesquisar", "busque", "buscar", "procure", "procurar"]
    if any(p in comando for p in palavras_pesquisa):
        resposta = pesquisar(comando)
        if resposta:
            falar(resposta)
        continue  

    resposta = comandos_personalizados(comando)

    if not resposta:
        resposta = executar_comandos(comando)

    if not resposta:
        resposta = abrir_youtube(comando)

    if not resposta:
        resposta = perguntar_ia(comando)

    if resposta:
        falar(resposta)