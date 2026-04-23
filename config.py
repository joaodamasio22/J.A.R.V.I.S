ASSISTANT_NAME = "Jarvis"
USER_NAME = "João"
 
TTS_VOICE      = "pt-BR-AntonioNeural"
TTS_TEMP_FILE  = "voz_temp.mp3"
 
STT_LANGUAGE          = "pt-BR"
STT_ENERGY_THRESHOLD  = 400
STT_PAUSE_THRESHOLD   = 0.8
STT_PHRASE_THRESHOLD  = 0.3
STT_NON_SPEAKING      = 0.5
STT_LISTEN_TIMEOUT    = 6
STT_PHRASE_LIMIT      = 8
STT_AMBIENT_DURATION  = 0.5
 
AI_API_KEY    = "SUA_CHAVE_AQUI"          # ← Troque aqui
AI_BASE_URL   = "https://openrouter.ai/api/v1"
AI_MODEL      = "openrouter/auto"
AI_MAX_TOKENS = 150
AI_RETRIES    = 3
AI_RETRY_WAIT = 2  
 
AI_SYSTEM_PROMPT = (
    "Você é {assistant}, assistente pessoal de {user}. "
    "Responda sempre em português, de forma direta e curta. Máximo 2 frases. "
    "Data e hora atual: {datetime}."
)
 
PROGRAMS = {
    "chrome":     r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "vscode":     r"C:\Users\User\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    "explorador": r"C:\Windows\explorer.exe",
    "spotify":    r"C:\Users\User\AppData\Roaming\Spotify\Spotify.exe",
    "cs2":        r"C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike 2\cs2.exe",
}
 
import os
FILE_SEARCH_PATHS = [
    os.path.expanduser("~\\Desktop"),
    os.path.expanduser("~\\Documents"),
    os.path.expanduser("~\\Downloads"),
    r"C:\Program Files",
    r"C:\Program Files (x86)",
]

LOG_LEVEL = "DEBUG"   
LOG_FILE  = "jarvis.log"
 