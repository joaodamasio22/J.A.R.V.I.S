import datetime
import webbrowser

def executar_comandos(comando):
    
    if "hora" in comando:
        hora = datetime.datetime.now().strftime("%H:%M")
        return f"agora são: {hora}"
        
    elif "ano" in comando:
        ano = datetime.date.now().year
        return f"estamos no ano de {ano}"
    
    elif "youtube" in comando:
        webbrowser.open("https://youtube.com")
        return "abrindo youtube..."
    
    return None

def abrir_youtube(comando):
    if "youtube" in comando:
        pesquisa = comando.replace("youtube", "")
        
        url = f"https://www.youtube.com/results?search_query={pesquisa}"
        
        webbrowser.open(url)
        
        return f"abrindo youtube {pesquisa}"
    
    return None