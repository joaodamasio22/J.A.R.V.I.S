import speech_recognition as sr

def ouvir():

    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 300
    recognizer.pause_threshold = 1.2

    with sr.Microphone() as source:

        print("Ajustando ao ruído ambiente...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        print("Jarvis ouvindo...")

        audio = recognizer.listen(
            source,
            timeout=5,
            phrase_time_limit=10
        )

    try:
        comando = recognizer.recognize_google(audio, language="pt-BR")
        print("Você disse:", comando)

        return comando.lower()

    except sr.UnknownValueError:
        print("Não entendi.")
        return ""

    except sr.RequestError:
        print("Erro no serviço de reconhecimento.")
        return ""