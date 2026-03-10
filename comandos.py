import ollama

def perguntar_ia(pergunta):

    resposta = ollama.chat(
        model="llama3",
        messages=[
            {"role": "system", "content": "Você é Jarvis, assistente do João."},
            {"role": "user", "content": pergunta}
        ]
    )

    return resposta["message"]["content"]

def comandos_personalizados(comando):
    
    comando = comando.lower()
    
    if "jarvis esta ai" in comando or "jarvis ta ai" in comando:
        return("ola joão, estou aqui, o que deseja?")
    
    elif "bom dia" in comando:
        return("Bom dia chefe, como você está?")
    
    elif "bom tarde" in comando:
        return("Bom tarde chefe, como você está?")
    
    elif "boa noite" in comando:
        return("Boa noite chefe, como você está?")
    
    return None