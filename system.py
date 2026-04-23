# system.py
import subprocess
import os

def executar_comandos(comando):
    """
    Aqui você pode colocar caminhos fixos de programas como Chrome, VSCode etc.
    """
    comando = comando.lower()
    
    programas = {
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "vscode": r"C:\Users\User\AppData\Local\Programs\Microsoft VS Code\Code.exe",
        "explorador": r"C:\Windows\explorer.exe",
        "spotify": r"C:\Users\User\AppData\Roaming\Spotify\Spotify.exe"
    }
    
    for nome, caminho in programas.items():
        if nome in comando:
            try:
                subprocess.Popen([caminho])
                return f"Abrindo {nome}"
            except Exception as e:
                return f"Erro ao abrir {nome}: {e}"
    
    return None

def abrir_youtube(comando):
    """
    Abrir links ou pesquisar vídeos no YouTube.
    """
    import webbrowser
    if "youtube" in comando:
        webbrowser.open("https://www.youtube.com")
        return "Abrindo YouTube"
    return None

def tocar_youtube(musica):
    import webbrowser
    url = f"https://www.youtube.com/results?search_query={musica.replace(' ','+')}"
    webbrowser.open(url)
    return f"Tocando {musica} no YouTube"

def tocar_spotify(musica):
    """
    Abre o Spotify app e pesquisa a música na web se quiser.
    """
    try:
        spotify_path = r"C:\Users\User\AppData\Roaming\Spotify\Spotify.exe"
        subprocess.Popen([spotify_path])
        return f"Tocando {musica} no Spotify"
    except Exception as e:
        return f"Erro ao abrir Spotify: {e}"

def iniciar_cs(comando):
    """
    Abre o CS2 pelo caminho do .exe ou Steam URI
    """
    comando = comando.lower()
    if "cs" in comando or "counter-strike" in comando or "jogar" in comando:
        try:
            cs_path = r"C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike 2\cs2.exe"
            # Para Steam URI, substitua por: subprocess.Popen(["steam://rungameid/ID_DO_CS2"], shell=True)
            subprocess.Popen([cs_path])
            return "Iniciando Counter-Strike"
        except Exception as e:
            return f"Erro ao abrir Counter-Strike: {e}"
    return None

# --- FUNÇÃO PARA ABRIR ARQUIVOS OU PROGRAMAS QUALQUER ---
def abrir_arquivo_ou_programa(nome_arquivo):
    """
    Pesquisa no PC e abre arquivos ou programas, diferenciando .exe de arquivos comuns
    """
    caminho = procurar_arquivo(nome_arquivo)
    
    if caminho:
        try:
            if caminho.lower().endswith(".exe"):
                subprocess.Popen([caminho])
            else:
                os.startfile(caminho)
            return f"Abrindo {nome_arquivo}"
        except Exception as e:
            return f"Erro ao abrir {nome_arquivo}: {e}"
    else:
        return f"Arquivo {nome_arquivo} não encontrado"

# --- FUNÇÃO PARA PROCURAR ARQUIVO NO PC ---
def procurar_arquivo(nome_arquivo, raiz="C:\\"):
    pastas_comuns = [
        os.path.expanduser("~\\Desktop"),
        os.path.expanduser("~\\Documents"),
        os.path.expanduser("~\\Downloads"),
        r"C:\Program Files",
        r"C:\Program Files (x86)",
    ]
    
    for pasta in pastas_comuns:
        for root, dirs, files in os.walk(pasta):
            for file in files:
                if nome_arquivo.lower() in file.lower():
                    return os.path.join(root, file)
    
    return None