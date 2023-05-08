import speech_recognition as sr
import pyttsx3 
import datetime 
import pywhatkit as pt
import calculos as operaciones
import saludos


def hablar(text):
    engine.say(text)
    engine.runAndWait()

while(True):
    engine = pyttsx3.init()
    engine.setProperty("rate", 180)
    listen = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
            voz = listen.listen(source)
            audio = listen.recognize_google(voz, language="es-ES").lower()
            hora = datetime.datetime.now().strftime("%I:%M") 
            res = operaciones.getResult(audio)
            hablar(res)
    except:
        hablar("note entendi")
        
    if "hola emma" in audio:
        hablar("hola juan, como estas")
    
    if "escribir" in audio:
        print("escribiendo")
        
    if "bien" in audio:
        hablar("me alegro")

    elif "hora" in audio:
        hablar(f"son las {hora}")     
    if "reproduce" in audio:
        music = audio.replace("reproduce", "")
        hablar("reproduciendo" + music) 
        pt.playonyt(music)
        
    if "buscar" in audio: 
        buscar = audio.replace("buscar"," ")
        hablar("buscando" + buscar)
        pt.search(buscar)

    if "apagar" in audio:
        hablar("apagando")
        quit(engine)