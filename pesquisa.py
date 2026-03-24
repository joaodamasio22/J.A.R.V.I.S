import webbrowser

def pesquisar(comando):
    palavras_chave = ["pesquisar", "pesquise", "buscar", "busque", "procurar", "procure"]
    
    encontrou = False
    for palavra in palavras_chave:
        if palavra in comando:
            encontrou = True
            break  
    
    if not encontrou:
        return None

    assunto = comando
    for p in palavras_chave:
        assunto = assunto.replace(p, "")
    assunto = assunto.strip()

    if not assunto:
        return "O que voce quer que eu pesquise?"

    webbrowser.open(f"https://www.google.com/search?q={assunto}")
    return f"Pesquisando sobre {assunto}"