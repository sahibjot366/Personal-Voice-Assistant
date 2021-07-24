import pyttsx3
import datetime
import speech_recognition as sr
from tkinter import *
from PIL import Image,ImageTk
import wikipedia
import webbrowser
import os
import json
import winsound
import random
import pygame
import smtplib
import pickle
import requests

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

ct=0
reminders={}
songs=[]
cdr=os.getcwd()
emails=['sahibjot366@gmail.com','sahibjot7180@gmail.com','faltukam7189@gmail.com']

def speak(audio):
    ''' Converts text to speech '''
    engine.say(audio)
    engine.runAndWait()


def init_microphone():
    ''' Initializes Microphone and Recognize audio and returns the audio in string form '''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold=2500
#         r.pau
        r.adjust_for_ambient_noise(source, duration=1)
#         speak("speak")
        print("Listening..")
        audio=r.listen(source)
        try:
            query=r.recognize_google(audio,language='en-in').lower()
        except:
            return "none"
        return query
    
def sendEmail(to,what_say):
    with open("location.txt","rb") as fh:
        loc=pickle.load(fh)
    os.chdir(loc)
    with open("password.txt","rb") as fh:
        passw=pickle.load(fh)
    os.chdir(cdr)
    for i in emails:
        if to in i:
            server=smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login('sahibjot7180@gmail.com',passw)
            server.sendmail('sahibjot7180@gmail.com',i,what_say)
            server.quit()
            break
    else:
        speak("Error.. Error..Email not found")
        print("Email not found")
        
def take_command():
    ''' Takes command and executes it '''
    run=1
    while run:
        task=init_microphone()
        print(task)
        
        speak("Please wait.. Working on your command..Just a second")
        
        if ("open google" in task)or("google" in task):
            run=0
            webbrowser.open("google.com")
        
        elif ("on youtube" in task) and ("search " in task):
            run=0
            task=task.replace("on youtube","")
            task=task.replace("search ","")
            task=task.replace(" ","+")
            webbrowser.open("https://www.youtube.com/results?search_query="+task)   
            
        elif "google duo" in task:
            webbrowser.open("https://duo.google.com/?web&utm_source=marketing_page_button_top")
            
        elif "shutdown computer" in task:
            run=0
            os.system("shutdown /s /t 1")
            
        elif "restart computer" in task:
            run=0
            os.system("shutdown /r /t 1")
            
        elif ("open youtube" in task)or ("youtube" in task):
            run=0
            webbrowser.open("youtube.com")
            
        
        elif "wikipedia" in task:
            run=0
            speak("Searching wikipedia.. Please wait..")
            task=task.replace("wikipedia","")
            tex=wikipedia.summary(task,sentences=5)
            print(len(tex))
            text=" "
            for i in range(len(tex)):
                if i%100!=0:
                    text=text+tex[i]
                else:
                    text=text+tex[i]+"-"+"\n"+"-"
            speak("According to Wikipedia..")
            print(text)
            speak(tex)
            
        elif "bluestacks" in task:
            run=0
            os.startfile("C:\ProgramData\BlueStacks\Client\Bluestacks.exe")
            
        elif "songs folder" in task:
            run=0
            os.startfile("C:\\Users\\sahib\\Desktop\\songs")
            
        elif task=="none":
            run=1
            speak("I did not Listened your command.. Please Speak Again")
        
        elif "open whatsapp" in task:
            run=0
            webbrowser.open("https://web.whatsapp.com/")
            
        elif "open eclipse" in task:
            run=0
            os.startfile("C:\\Users\\sahib\\eclipse\\java-2020-03\\eclipse\\eclipse.exe")
            
        elif "open zoom" in task:
            run=0
            os.startfile("C:\\Users\\sahib\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
            
        elif "open downloads" in task:
            run=0
            os.startfile("C:\\Users\\sahib\\Downloads")
            
        elif "thank you" in task:
            run=0
            speak("It's my pleasure!!")
            speak("I like helping you Sir..")
            
        elif "my name" in task:
            run=0
            speak("Your name is")
            speak("Sahibjot Singh Aneja")
            
        elif "your name" in task:
            run=0
            speak("My name is Eagle Assistant..")
            speak("If you want to do anything in this PC I will help you")
            
        elif ("open chrome" in task) or ("open google chrome" in task):
            run=0
            os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
            
        elif "time" in task:
            run=0
            hr=datetime.datetime.now().hour
            mint=datetime.datetime.now().minute
            if hr>=1 and hr<12:
                speak("The Time is : ")
                speak(f"{hr}:{mint} A M")
            elif hr==24 or hr==0:
                hr=12
                speak("The Time is : ")
                speak(f"{hr}:{mint} A M")
            elif hr==12:
                speak("The Time is : ")
                speak(f"{hr}:{mint} P M")
            else:
                hr=hr-12
                speak("The Time is : ")
                speak(f"{hr}:{mint} P M")
        
        elif "open code blocks" in task:
            run=0
            os.startfile("C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe")
            
        elif "open turbo c" in task:
            run=0
            os.startfile("C:\\YOGISOFT\\Turboc8.exe")
        
        elif "open notepad" in task:
            run=0
            os.startfile("C:\\Users\\sahib\\Desktop\\Notepad++\\notepad++.exe")
        
        elif "open visual studio code" in task:
            run=0
            os.startfile("C:\\users\\sahib\\AppData\\Local\\Programs\\Microsoft VS Code\\Code")
            
        elif ("please quit" in task) or ("please exit" in task) or("quit" in task) or ("exit" in task):
            run=0
            speak("Making an Exit!!")
            speak("Just A Second")
            speak("Ok Sir!! Have a nice day")
            exit(0)
            
        elif ("set a reminder" in task) or ("set reminders" in task) or ("set reminder" in task):
            run=0
            speak("Tell Me,What should I remind for ?")
            what=init_microphone()
            speak("Please wait !!")
            print("please wait")
            while True:
                if what=="none":
                    speak("I Did Not understood!! Please say it again")
                    what=init_microphone()
                    speak("Please wait !!")
                else:
                    break
            if "please remind me to" in what:
                what=what.replace("please remind me to","")
            if "remind me to" in what:
                what=what.replace("remind me to","")
                
            print(what)
            speak("At what Time I should Remind You ?")
            
            while True:
                tim=init_microphone()
                speak("Please wait !!")
                print("please wait")
                while True:
                    if tim=="none":
                        speak("I Did Not understood!! Please say it again")
                        tim=init_microphone()
                    else:
                        break
                print(tim)
                try:
                    spt=tim.split(" ")
                    hrmin=spt[0].split(":")
                    break
                except:
                    speak("Sorry,I couldn't understand time")
                    speak("Please repeat it ")
            
            with open("reminders.txt") as fh:
                reminders=json.load(fh)
                
            if spt[1]=="a.m." and hrmin[0]==12:
                timer=f"{24}:{hrmin[1]}"
                reminders.update({what:timer})
                speak("Reminder successfully set")
            elif spt[1]=="a.m.":
                timer=f"{hrmin[0]}:{hrmin[1]}"
                reminders.update({what:timer})
                speak("Reminder successfully set")
            elif spt[1]=="p.m." and hrmin[0]==12:
                timer=f"{12}:{hrmin[1]}"
                reminders.update({what:timer})
                speak("Reminder successfully set")
            else:
                timer=f"{int(hrmin[0])+12}:{hrmin[1]}"
                reminders.update({what:timer})
                speak("Reminder successfully set")
            with open("reminders.txt","w") as fh:
                    json.dump(reminders,fh)
                
        elif "show reminders" in task:
            run=0
            with open("reminders.txt") as fh:
                speak("Here Are all the Reminders..")
                print(json.load(fh))
                
        elif ("play music" in task) or ("play song" in task) or ("play songs" in task):
            run=0
            os.chdir("C:\\Users\\sahib\\Desktop\\songs")
            song_list=os.listdir("C:\\Users\\sahib\\Desktop\\songs")
            con=True
            while con:
                d=random.choice(song_list)
                if d in songs:
                    pass
                elif song_list==songs:
                    speak("All the Songs have been Played")
                    os.chdir(cdr)
                    break
                else:
                    songs.append(d)
                    pygame.mixer.init()
                    pygame.display.init()
                    pygame.mixer.music.load(d)
                    pygame.mixer.music.set_endevent(pygame.USEREVENT)
                    pygame.mixer.music.play()
                    running=True
                    while running:
                        comm=init_microphone()
                        if "pause" in comm:
                            pygame.mixer.music.pause()
                        elif "resume" in comm:
                            pygame.mixer.music.unpause()
                        elif "quit" in comm:
                            pygame.mixer.music.stop()
                            running=False
                            con=False
                            os.chdir(cdr)
                            break
                        elif ("next" in comm) or ("skip" in comm):
                            running=False
                            pygame.mixer.music.stop()
                            break
                        else:
                            pass
                        for event in pygame.event.get():
                            if event.type==pygame.USEREVENT:
                                running=False
                                pygame.mixer.stop()
                                break
        
        elif ("send mail" in task) or ("send email" in task) or("send e mail" in task)or("send e-mail" in task):
            run=0
            try:
                speak("To whom you want To send E Mail ?")
                while True:
                    to=init_microphone()
                    if to=="none":
                        speak("I was not able to listen properly, Please speak again")
                    else:
                        break
                print(to)
                speak("What shouls I Say ?")
                while True:
                    what_say=init_microphone()
                    if what_say=="none":
                        speak("I was not able to listen properly, Please speak again")
                    else:
                        break
                sendEmail(to,what_say)
                speak("E Mail has been succesfully sent")
            except:
                speak("Sorry Bro, I was unable to send Email")
                
        elif "delete all reminders" in task:
            run=0
            with open("reminders.txt","w") as fh:
                fh.write("{}")
                
        elif ("delete last reminder" in task) or ("delete reminder" in task):
            run=0
            with open("reminders.txt") as fh:
                reminders=json.load(fh)
            reminders.popitem()
            
            with open("reminders.txt","w") as fh:
                json.dump(reminders,fh)
        
        elif ("check weather" in task) or ("weather report" in task):
            run=0
            speak("For which city do you want to check weather?")
            while True:
                city=init_microphone()
                if city=="none":
                    speak("I did not understood.. Please speak again")
                else:
                    break
            
            BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
            API_KEY ="42bed5081194f2c724235481f8d90139"
            URL = BASE_URL + "q=" + city + "&appid=" + API_KEY+"&units=metric"
            report=requests.get(URL).json()
            print(f"{city} weather report : {report['weather'][0]['description']};\nTemperature is expected to be {report['main']['temp']} Celsius\n; Temperature range from {report['main']['temp_min']} to {report['main']['temp_max']}  Celsius ;\nWind speed is {report['wind']['speed']} m/s;\n humidity is {report['main']['humidity']} %\n and pressure is {report['main']['pressure']} hpa")
            speak(f"{city} weather report : {report['weather'][0]['description']};Temperature is expected to be {report['main']['temp']} degree Celsius; Temperature range from {report['main']['temp_min']} to {report['main']['temp_max']} degree Celsius ;,Wind speed is {report['wind']['speed']} metre per second;, humidity is {report['main']['humidity']} percent and pressure is {report['main']['pressure']} hpa")
        else:
            run=0
            webbrowser.open("http://google.com/?#q="+task)
        

def hello():
    ''' Wishes me when it gets started '''
    global ct
    if ct==0:
        time=datetime.datetime.now().hour
        if time >=0 and time<12:
            speak("Good Morning Sir!!")
        elif time>=12 and time<17:
            speak("Good Afternoon Sir!!")
        else:
            speak("Good Evening Sir!!")
        speak("I am Eagle")
        speak("How may I help you?")
        ct+=1
    else:
        speak("Sir!!")
        speak("Tell me a task to perform ")
        
def eagle_logo():
    ''' To show Eagle logo GUI on screen '''
    hello()
    root=Tk()
    root.geometry("480x360")
    root.minsize("480","360")
    root.maxsize("480","360")
    image=Image.open("eagle.png")
    photo=ImageTk.PhotoImage(image)
    la=Label(image=photo)
    la.pack()
    lp=Label(text="let me initialize everything..")
    lp.pack()
    l=Label(text="Please speak after 1 sec of terminatiion of this window")
    l.pack()
    root.after(1500, lambda: root.destroy())
    root.mainloop()

if __name__ == "__main__":

    while True:
        with open("reminders.txt") as fh:
            rem=json.load(fh)
        hours=datetime.datetime.now().hour
        minutes=datetime.datetime.now().minute
        if minutes//10>0:
            currtime=f"{hours}:{minutes}"
        else:
            currtime=f"{hours}:0{minutes}"
        for i,j in rem.items():
            if (j==currtime):
                speak("Reminder!!Reminder!!")
                winsound.Beep(440,1500)
                speak(i)
        winsound.Beep(500,120)
        query=init_microphone()
        if "eagle" in query:
            eagle_logo()
            take_command()
            
        else:
            pass