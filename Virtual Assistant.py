# Import Packages
import pyttsx3
import speech_recognition as sr
import subprocess
# from Features import YoutubeSearch
import Features
# =============================================

# Changing Assistant Sound to Female
Engine = pyttsx3.init()
Voices = Engine.getProperty("voices")
Engine.setProperty("voice", Voices[1].id)
Engine.setProperty('rate',170)


# Speak Function For Command


def Speak(Command):
    Engine.say(Command)
    Engine.runAndWait()

def Listen(Message):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("=============================")
        print(f"Say Something! ({Message}) 🔊")
        print("=============================")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        Query = r.recognize_google(audio)
        # print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
        return Query.lower()
    except:
        return ""
# Speak("Hello World");
# Listen();


def Tasks():
    Results = Listen("Listening")


    if "youtube search" in Results:
        Tokenize = Results.replace("youtube search", "")
        Features.YoutubeSearch(Tokenize)
    elif "google search" in Results:
        Tokenize = Results.replace("google search", "")
        Features.GoogleSearch(Tokenize)
    elif "download this video" in Results:
        Features.DownloadVideo();
    elif "test internet speed" in Results:
        Features.SpeedTest();
    elif "calculate" in Results:
        Tokenize = Results.replace("calculate", "")
        Tokenize=Tokenize.replace("divided by","/")
        Tokenize=Tokenize.replace("x","*")
        Features.Calculator(Tokenize)
    elif "whatsapp message" in Results:
        Speak("Tell The Recipient Name");
        Name=Listen("Recording");
        print(f"--> User Name Is : {Name}")
        Speak("Record Your Message")
        Message=Listen();
        print(f"--> Message Is : {Message}")
        Features.WhatsappMessage(Name,Message)
    elif "open" in Results:
        Tokenize=Results.replace("open","");
        Features.RunProgramme(Tokenize)
    elif "lisa" in Results and ("hello" in Results or "hey" in Results):
        Features.Respond()
    # ==============Window Context=================

    elif "show" in Results and "window" in Results:
        # Tokenize=Results.replace("show window","");
        Tokenize=Results.split();
        Features.ShowWindow(Tokenize[-1])
    elif "close" in Results and "window" in Results:
        Features.CloseWindow()
    elif ("minimise" in Results or "minimize" in Results) and "window" in Results:
        Features.MinimizeWindow()
    elif ("maximise" in Results or "maximize" in Results) and "window" in Results:
        Features.MaximizeWindow()

    # ==============Volume Control=================
    elif "mute" in Results:
        Features.MuteAudio()
    elif "increase" in Results and "times" in Results:
        Features.IncreaseAudio(Results)
    elif "decrease" in Results and "times" in Results:
        Features.DecreaseAudio(Results)

    # ==============Wi-Fi Control=================
    elif "on" in Results and ("wifi" in Results or "wi-fi" in Results):
        Features.TurnOnWiFi()
    elif "off" in Results and ("wifi" in Results or "wi-fi" in Results):
        Features.TurnOffWiFi()

    # ==============Jokes API=================
    elif "joke" in Results :
        Features.TellJoke()
    # ===========Functionalities==============
    elif "screenshot" in Results or "snapshot" in Results or "screen shot" in Results or "snap shot" in Results :
        Features.ScreenShot()
    elif "time" in Results :
        Features.CurrentTime()
    elif "note" in Results:
        Speak("Record Your Note, Go Ahead");
        Note = Listen("Recording")
        Features.WriteNote(Note)
    elif "weather" in Results :
        Features.Weather()
        
    elif len(Results)==0:
        return ""
    else:
        try:
            Features.Google(Results)
        except: 
            Speak("Google Speech Recognition Could Not Understand Audio or May Be Network Issue")

while 1:
    Tasks()