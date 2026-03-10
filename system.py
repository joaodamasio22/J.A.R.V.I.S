import subprocess
import webbrowser
import urllib.parse

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

    busca = musica.replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={busca}"
    webbrowser.open(url)
    return f"Buscando {musica} no YouTube"


def tocar_spotify(musica):
    
    musica_codificada = urllib.parse.quote(musica)
    
    uri = f"spotify:search:{musica_codificada}"
    
    try:
        subprocess.Popen([r"C:\Users\User\AppData\Roaming\Spotify\Spotify.exe", uri])
        return f"Buscando por {musica} no spotify"
    except Exception as e:
        return f"Erro ao abrir Spotify: {e}"
    
def iniciar_cs(comando):

    if not comando:
        return None

    comando = comando.lower()

    if "cs" in comando or "counter-strike" in comando or "jogar" in comando:
        try:
            
            cs_path = r"C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike 2\cs2.exe"
            subprocess.Popen([cs_path])
            return "Iniciando Counter-Strike"
        except Exception as e:
            return f"Erro ao abrir o Counter-Strike: {e}"