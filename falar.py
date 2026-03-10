import pyttsx3 as p3

def falar(texto):
    engine = p3.init()
    
    engine.say(texto)
    
    engine.runAndWait()