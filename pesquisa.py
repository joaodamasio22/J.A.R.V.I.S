import webbrowser

def pesquisar(comando):
    for palavra in ["pesquisar", "pesquise", "buscar", "busque"]:
         
        if palavra in comando:
            assunto = comando
            
            for p in ["pesquisar", "pesquise", "buscar", "busque"]:
                assunto = assunto.replace(p, "")
            
            assunto = assunto.strip()

            webbrowser.open(f"https://www.google.com/search?q={assunto}")

            return f"Pesquisa concluída sobre {assunto}"

        return None