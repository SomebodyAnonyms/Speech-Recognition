import speech_recognition as sr

def Recognition():
    Detection = False
    while not Detection:
        try:
            print("i'm listening to you...")
            Recognizer = sr.Recognizer()
            Microphone = sr.Microphone()
            with Microphone as source: Audio = Recognizer.listen(source)
            Speech_Result = Recognizer.recognize_google(Audio)
            Detection = True
            return Speech_Result
        except:
            print("Not understood. Please say again")

print("You Said: " + Recognition())
