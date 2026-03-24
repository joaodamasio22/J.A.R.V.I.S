from openai import OpenAI
from datetime import datetime
import time

client = OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1"
)

def perguntar_ia(pergunta):
    agora = datetime.now()
    data_hora = agora.strftime("%A, %d de %B de %Y, %H:%M")
    
    for tentativa in range(3):
        try:
            resposta = client.chat.completions.create(
                model="openrouter/auto",
                messages=[
                    {"role": "system", "content": f"""Voce e Jarvis, assistente pessoal do Joao.
Responda sempre em portugues, de forma direta e curta. Maximo 2 frases.
Data e hora atual: {data_hora}
Dia da semana em portugues: {agora.strftime('%A')}"""},
                    {"role": "user", "content": pergunta}
                ]
            )
            return resposta.choices[0].message.content
        except Exception as e:
            print(f"Tentativa {tentativa+1} falhou: {e}")
            time.sleep(2)
    return "Desculpe Joao, estou com problemas no momento."

def comandos_personalizados(comando):
    comando = comando.lower()

    agora = datetime.now()
    if any(p in comando for p in ["que dia", "que horas", "hora certa", "data"]):
        if "hora" in comando:
            return f"Sao {agora.strftime('%H:%M')} Joao."
        else:
            return f"Hoje e {agora.strftime('%d/%m/%Y')}, {agora.strftime('%A')}."

    if any(p in comando for p in ["ta ai", "esta ai", "esta aqui", "ta aqui"]):
        return "Ola Joao, estou aqui, o que deseja?"
    elif "bom dia" in comando:
        return "Bom dia chefe, como voce esta?"
    elif "boa tarde" in comando:
        return "Boa tarde chefe, como voce esta?"
    elif "boa noite" in comando:
        return "Boa noite chefe, como voce esta?"
    elif any(p in comando for p in ["tudo certo", "tudo bem", "como vai"]):
        return "Tudo otimo por aqui Joao, e voce?"

    return None