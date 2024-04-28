import os
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is ")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("Today's date is ")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back Sir.")
    date()
    time()
    #create an hour variable
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 16:
        speak("Good afternoon!")
    elif hour >= 16 and hour < 21:
        speak("Good evening!")
    else:
        speak("Goodnight!")
    speak("How may I assist you?")

def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recogniziing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again!")
        return "None"
    
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('nana@gmail.com','********')
    server.sendmail('nana@gmail.com', to, content)
    server.close()

def takeScreenshot():
    img = pyautogui.screenshot()
    img.save('C:\\Users\\Eben\\Downloads\\pics\\ss.png')

def cpu_battery():
    usage = str(psutil.cpu_percent())
    speak("CPU is at " + usage)
    battery = psutil.sensors_battery()
    speak("battery is at " + battery.percent)

def jokes():
    speak(pyjokes.get_joke())

# Main function
if __name__ == "__main__":
    wishme()

    while True:
        query = takeCommand()

        if 'time' in query:
            time()
        
        elif 'date' in query:
            date()

        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak("What is your message?")
                content = takeCommand()
                to = 'nanaquofitabi94@gmail.com'
                #sendEmail(to, content)
                #speak("Email sent successfully")  
                speak("Send email demo.")

            except Exception as e:
                print(e)  
                speak("Unable to send email.")
        
        elif 'search in chrome' in query:
            speak("What should I search?")
            chrome_path = 'path..... %s'
            search = takeCommand()
            wb.get(chrome_path).open_new_tab(search + '.com')
        
        elif 'logout' in query:
            os.system("shutdown -l")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'play songs' in query:
            songs_dir = r'C:\Users\Eben\Downloads\Music'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif 'remember that' in query:
            speak('What should I remember?')
            data = takeCommand()
            speak('You asked me to remember that'+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()

        elif 'do yo remeber anything' in query:
            remember = open('data.txt', 'r')
            speak("you asked me to rem ember that" + remember.read())


        elif 'screenshot' in query:
            speak("Alright! Taking a screenshot now!")
            takeScreenshot()
            speak("Screenshot taken successfully!")
        
        elif 'cpu and battery' in query:
            cpu_battery()
        
        elif 'joke' in query:
            jokes()

        elif "shutdown" in query:
            speak("Okay Sir! Shutting down now. Talk to you soon. Take care Nana Kofi")
            quit()