#DINESHSAGAR

#If the code is not working or have any issues with path, get in touch with me.

import speech_recognition as sr

r2 = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r2.listen(source)
    try:
        text = r2.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said")