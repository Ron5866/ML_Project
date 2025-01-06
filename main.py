import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may i help you")


def takeCommand():
    # it takes microphone input from the user and return the string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold =1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):  # enable less secure app for which account you will be sending the email
    # server = smtplib.SMTP('smtp.gmail.com', 587)
    # server.ehlo()
    # server.starttls()
    # server.login('youremail@gmail.com',your=password)
    # server.sendmail('youremail@gmail.com', to,content)
    # server,close()

    if __name__ == "__main__":
        wishme()
        while True:
            query = takeCommand().lower()

            # logic for executing task based on query
            if 'wikipiedia' in query:
                speak("Seachering wikipedia...")
                query = query.replace("wikipedia", '')
                results = wikipedia.summary(query, sentences=3)
                speak("According to wikipedia")
                print(results)
                speak(results)
            elif 'open youtube' in query:
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                webbrowser.open("google.com")

            elif 'open gmail' in query:
                webbrowser.open("gmail.com")

            elif 'open whatsapp' in query:
                appPath = 'Whatapp'
                os.startfile(appPath)


            # elif 'play music' in query:
            # music_dir = "path"
            # songs = os.listdir(music_dir)
            # print(songs)
            # os.startfile(os.path.join(music_dir, songs[0]))

            elif 'the time' in query:
                strTime = datetime.dttetime.now().strftime('%H:%M:%S')
                speak(f"Sir, the Time is {strTime}")

            elif 'open code' in query:
                codePath = "C:\\Users\\DEEP\\AppData\\Local\\Programs\\Microsoft VS Code\Code.exe"
                os.startfile(codePath)
            # make dictionary in begining where key will be the name and values will be their email_id
            elif 'send email' in query:
                try:
                    speak("What should i say?")
                    content = takeCommand()
                    to = "nameyouremail@gmail.com"
                    sendEmail(to, content)
                    speak("EMail has been sent")
                except Exception as e:
                    print(e)
                    speak('Sorry bro, something went wrong')

            elif 'quit' or 'bye' in query:
                speak("Quiting Sir! Thank you for your Time")
                break
