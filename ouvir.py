import speech_recognition as sr
import time

def ouvir():
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 400      
    recognizer.pause_threshold = 0.8       
    recognizer.phrase_threshold = 0.3      
    recognizer.non_speaking_duration = 0.5 

    with sr.Microphone() as source:
        print("🎤 Ajustando ao ruído...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)  
        print("👂 Jarvis ouvindo...")

        try:
            audio = recognizer.listen(
                source,
                timeout=6,
                phrase_time_limit=8
            )
        except sr.WaitTimeoutError:
            return ""  

    try:
        comando = recognizer.recognize_google(audio, language="pt-BR")
        print(f"✅ Você disse: {comando}")
        return comando.lower()

    except sr.UnknownValueError:
        print("❓ Não entendi.")
        return ""

    except sr.RequestError as e:
        print(f"🔴 Erro no serviço: {e}")
        return ""