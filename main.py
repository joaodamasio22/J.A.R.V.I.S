from falar import falar
from ouvir import ouvir
import webbrowser
import datetime

while True:
    comando = ouvir()
    
    if "jarvis" in comando:
        falar("Olá João, estou ouvindo.")
        
    elif "hora" in comando:
        hora = datetime.now().strftime("%H:%M")
        falar(f"agora é exatamente {hora}.")
        
    elif "youtube" in comando:
        falar("iniciando youtube...")
        webbrowser.open("https://www.youtube.com")
        
    elif "google" in comando:
        falar("abrindo google...")
        webbrowser.open("https://www.google.com")
        
    elif "github" in comando:
        falar("abrindo github...")
        webbrowser.open("https://www.github.com")
        
    elif "sair" in comando:
        falar("finalizando sistema, até mais joão...")
        break
    