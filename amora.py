from io import FileIO
import pyttsx3
import speech_recognition as sr
from datetime import datetime 
import datetime
import datetime
import wikipedia
import webbrowser
# import Dictionaries
import os
import smtplib
import requests
from bs4 import BeautifulSoup
from wikipedia import exceptions
from wikipedia.wikipedia import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)  
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning !")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Allow me to introduce myself . I am Amora")
    speak("how can i help you")
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.adjust_for_ambient_noise(source)                
        print("Listening...")   
        # r.pause_threshold = 0.8
        # r.energy_threshold=300
        r.energy_threshold = 1000  # minimum audio energy to consider for recording
        r.dynamic_energy_threshold = True
        r.dynamic_energy_adjustment_damping = 0.15
        r.dynamic_energy_ratio = 1.5
        r.pause_threshold = 1  # seconds of non-speaking audio before a phrase is considered complete
        r.operation_timeout = None  # seconds after an internal operation (e.g., an API request) starts before it times out, or ``None`` for no timeout

        r.phrase_threshold = 0.3  # minimum seconds of speaking audio before we consider the speaking audio a phrase - values below this are ignored (for filtering out clicks and pops)
        r.non_speaking_duration = 0.5  # seconds of non-speaking audio to keep on both sides of the recording
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content): 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('amourcmrg@gmail.com',os.environ['pwsss'])
    server.sendmail('amourcmrg@gmail.com', to, content)                          
    server.close() 
    

if __name__ == "__main__":
    wishMe()
    while True: 
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentences=2)
            speak("resutls from Wikipedia tells that")
            print(results)
            speak(results)
            
        
        elif  'what is your name' in query:
            speak('my name is Amora and i am your virtual assistant')
            
        elif 'open youtube' in query:
            speak('opening youtube')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak('opening google')
            webbrowser.open("google.com")
            
        elif 'open spotify' in query:
            speak('opening spotify for you')
            webbrowser.open("https://open.spotify.com/playlist/37i9dQZEVXbMWDif5SCBJq")
            
        elif 'hungry' in query:
            speak("why don't you order delicious from this website")
            webbrowser.open('zomato.com')
            
        elif 'reserve' in query:
            speak("you can book you tickets from this website")
            webbrowser.open("makemytrip.com")
            
        elif 'games' in query:
            # random("poki.com","gogi.com","onlinegames.com")
            webbrowser.open("poki.com")
            speak('opening a gaming website')
            
        elif "read" in query:
            webbrowser.open("archive.org")
            speak("here you go")       

        elif 'open stack overflow' in query:
            speak('opening stack overflow')
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:         
            #music_dir =  "C:\\Users\\shais\\Downloads\\Stay-Justin-Bieber-Ft-The-Kid-Laroi-(TrendyBeatz.com).mp3"
            #music_dir = "C:\\Users\\shais\\Downloads\\Shawn_Mendes_X_Camila_Cabello.mp3"
            music_dir  = "C:\\Users\\shais\\Music\\Playlists"
            #music_dir  = ""
            
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))             

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"the current time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\shais\\Desktop\\Visual Studio Code.lnk"
            os.startfile(codePath)

        elif 'send email' in query:
            speak("whom do you want to send an email")      
            try:
                    query=takeCommand().lower()
                    if 'myself' in query:   
                        try:    
                            query=query.replace("me","")
                            speak(" okay, What should I say?")
                            content = takeCommand()
                            print(content)
                            to = "shaisthatarannum2003@gmail.com"
                            sendEmail(to, content)
                            speak("Email has been sent!")
                        except Exception as e:
                            print(e)
                            speak("Sorry sir . I am not able to send this email")
            
                    if 'ammar' in query:   
                        try:
                            query=query.replace("ammar","")
                            speak(" okay, What should I say?")
                            content = takeCommand()
                            print(content)
                            to = "md.ammaruddin2020@gmail.com"
                            sendEmail(to, content)
                            speak("Email has been sent!")
                        except Exception as e:
                            print(e)
                            speak("Sorry sir . I am not able to send this email")
                    if 'musa' in query:   
                        try:
                            query=query.replace("musa","")
                            speak(" okay, What should I say?")
                            content = takeCommand()
                            print(content)
                            to = "moosabaig06@gmail.com"
                            sendEmail(to, content)
                            speak("Email has been sent!")
                        except Exception as e:
                            print(e)
                            speak("Sorry sir . I am not able to send this email")
                    elif 'tanu' in query:   
                        try:
                            query=query.replace("tanu","")
                            speak(" okay, What should I say?")
                            content = takeCommand()
                            print(content)
                            to = "tanusreepamisetty@gmail.com"
                            sendEmail(to, content)
                            speak("Email has been sent!")
                        except Exception as e:
                            print(e)
                            speak("Sorry sir . I am not able to send this email")
                    elif 'everyone' in query:
                        try:
                            query=query.replace("everyone","")
                            speak(" okay, What should I say?")
                            content = takeCommand()
                            print(content)
                            to = "tanusreepamisetty@gmail.com","moosabaig06@gmail.com","shaisthatarannum2003@gmail.com","md.ammaruddin2020@gmail.com"
                            sendEmail(to, content)
                            speak("Email has been sent!")
                        except Exception as e:
                            print(e)
                            speak("Sorry sir . I am not able to send this email")
                        
            except exceptions as n:
                print(n)
                speak(" sorry, no friend found with such name")
                           

        elif "weather" in query :
                   speak("which city's temperature do you want to know?")
                   query=takeCommand().lower()
       
                   user_api = "20b568252d0701afed00a04428c41ed6"
                
                   location = query

                   complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
                   api_link = requests.get(complete_api_link)
                   api_data = api_link.json()

                    #create variables to store and display data
                   temp_city = ((api_data['main']['temp']) - 273.15)
                   weather_desc = api_data['weather'][0]['description']
                   hmdt = api_data['main']['humidity']
                   wind_spd = api_data['wind']['speed']
               

                   print ("Current temperature is: {:.2f} deg C".format(temp_city))
                   print ("Current weather desc  :",weather_desc)
                   print ("Current Humidity      :",hmdt, '%')
                   print ("Current wind speed    :",wind_spd ,'kmph')
                   speak(" the Current temperature of " + location+ "is{:.2f} degree celsius with humidity and wind speed status of {} percentage and {} kilometer per hour respectively".format(temp_city,hmdt,wind_spd))
                                 
        elif 'remember that' in query:
                   rememberMsg = query.replace("remember that ","")
                   rememberMsg = rememberMsg.replace("jarvis","")
                   speak(f"You told me to remind you that :"+rememberMsg)
                   remember = open('data.txt','w')
                   remember.write(rememberMsg)
                   remember.close()

        elif ' reminders ' in query:
               remember = open('data.txt','r')
               speak("You tell me to remind you that" + remember.read())         
               
            
        elif 'exit' in query:
                speak("okay, have a nice day")
                exit()