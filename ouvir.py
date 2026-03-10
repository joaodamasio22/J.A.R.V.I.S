import speech_recognition as sr

def ouvir():

    reconhecedor = sr.Recognizer()

    with sr.Microphone() as source:
        print("Ajustando microfone...")
        reconhecedor.adjust_for_ambient_noise(source, duration=1)

        print("Jarvis ouvindo...")
        audio = reconhecedor.listen(source)

        print("Processando áudio...")

    try:
        comando = reconhecedor.recognize_google(audio, language="pt-BR")
        print("Você disse:", comando)
        return comando.lower()

    except Exception as erro:
        print("Erro:", erro)
        print("Não entendi")
        return ""


ouvir()