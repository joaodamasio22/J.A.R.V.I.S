import webbrowser

def pesquisar(comando):

    if "pesquisar" in comando:

        assunto = comando.replace("pesquisar", "")

        webbrowser.open(f"https://www.google.com/search?q={assunto}")

        return f"Pesquisa concluída sobre {assunto}"

    return None