from ouvir import ouvir
from falar import falar

from comandos import perguntar_ia, comandos_personalizados
from system import executar_comandos, abrir_youtube, tocar_spotify, tocar_youtube
from pesquisa import pesquisar

import unidecode  

while True:
    comando = ouvir()
    if not comando:
        continue

    comando = unidecode.unidecode(comando.lower().strip())
    comando = comando.replace("jarvis", "").strip()

    resposta = None

    if "toca" in comando or "tocar" in comando or "reproduza" in comando:
        musica = comando.replace("toca", "").replace("tocar", "").replace("reproduza", "").replace("spotify", "").strip()
        
        if "spotify" in comando:
            resposta = tocar_spotify(musica)
        else:
            resposta = tocar_youtube(musica)
        
        falar(resposta)
        continue
        
    resposta = comandos_personalizados(comando)

    if not resposta:
        resposta = executar_comandos(comando)

    if not resposta:
        resposta = abrir_youtube(comando)

    if not resposta and "pesquise" in comando:
        resposta = pesquisar(comando)

    if not resposta and "sair" in comando:
        falar("Até mais chefe! finalizando sistemas...")
        break

    if not resposta:
        resposta = perguntar_ia(comando)

    if resposta:
        falar(resposta)