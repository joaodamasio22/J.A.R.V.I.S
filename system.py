import subprocess
import webbrowser
import os

def executar_comandos(comando):
    comando = comando.lower().strip()

    if "chrome" in comando:
        try:
            # Caminho padrão do Chrome no Windows
            subprocess.Popen(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
            return "Abrindo Google Chrome"
        except:
            return "Não consegui abrir o Chrome"

    elif "vscode" in comando or "visual studio code" in comando:
        try:
            subprocess.Popen(r"C:\Users\%USERNAME%\AppData\Local\Programs\Microsoft VS Code\Code.exe")
            return "Abrindo Visual Studio Code"
        except:
            return "Não consegui abrir o VSCode"

    elif "spotify" in comando:
        try:
            subprocess.Popen(r"C:\Users\User\AppData\Roaming\Spotify\Spotify.exe")
            return "Claro patrão, o que você deseja ouvir?"

        except:
            return "Não consegui abrir o Spotify"

    elif "explorador" in comando or "meus arquivos" in comando:
        try:
            subprocess.Popen("explorer")
            return "Abrindo o explorador de arquivos"
        except:
            return "Não consegui abrir o explorador"

    return None


def abrir_youtube(comando):
    """
    Abre YouTube no navegador
    """
    comando = comando.lower()
    if "youtube" in comando:
        webbrowser.open("https://www.youtube.com")
        return "Abrindo YouTube"
    return None


def tocar_youtube(musica):
    """
    Pesquisa e abre música no YouTube
    """
    busca = musica.replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={busca}"
    webbrowser.open(url)
    return f"Buscando {musica} no YouTube"


def tocar_spotify(musica):
    """
    Pesquisa e abre música no Spotify
    """
    busca = musica.replace(" ", "%20")
    url = f"https://open.spotify.com/search/{busca}"
    webbrowser.open(url)
    return f"Buscando {musica} no Spotify"

