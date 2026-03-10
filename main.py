from ouvir import ouvir
from falar import falar

from comandos import perguntar_ia
from comandos import comandos_personalizados

from system import executar_comandos
from system import abrir_youtube

from pesquisa import pesquisar


while True:

    comando = ouvir()
    
    if "jarvis" not in comando:
        continue
    
    comando = comando.replace("jarvis", "").strip()

    resposta_personalizada = comandos_personalizados(comando)
    resposta_sistema = executar_comandos(comando)
    resposta_youtube = abrir_youtube(comando)


    if resposta_personalizada:
        falar(resposta_personalizada)

    elif resposta_sistema:
        falar(resposta_sistema)

    elif resposta_youtube:
        falar(resposta_youtube)

    elif "pesquise" in comando:
        resposta = pesquisar(comando)
        falar(resposta)

    elif "sair" in comando:
        falar("Até mais chefe! finalizando sistemas...")
        break

    else:
        resposta = perguntar_ia(comando)

        print("JARVIS:", resposta)

        falar(resposta)