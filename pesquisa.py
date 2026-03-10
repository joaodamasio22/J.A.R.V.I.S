import webbrowser

def pesquisar(pergunta):
    
    url = (f"https://www.google.com/search?q={pergunta}")
    webbrowser.open(url)
    
    return "pensando..."