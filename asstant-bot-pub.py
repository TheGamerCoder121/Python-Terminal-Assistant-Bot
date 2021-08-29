#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 15:20:32 2021

@author: vegatechcomputerservices
"""
#! Python libraries
from __future__ import unicode_literals
import random
from datetime import datetime
from datetime import date
import datetime
from pyowm import OWM # import Python Open Weather Map to our project.
from sys import exit
from pyfiglet import Figlet # takes ASCII text and renders it in ASCII art fonts
from termcolor import colored # Creates colored text in console
import time
import pyjokes
import pyttsx3 # Offline Text To Speech (TTS) converter for Python
import urllib.request
import re
from pytube import YouTube
import youtube_dl

import pygame
import os

pygame.init()
os.system('cls')

#! Vars 
welcomeResponses = ["Howdy, partner!", "Whats up boss man?", "Ahoy, matey!", "Hiya!", "GOOOOOD MORNING, VIETNAM!", "I'm Batman.", "YOOOO"]

regularResponces = ["How can I help you?", "What do you need from me?", "How can I assist you?", "Choose a option from the list from below"]

errorResponces = ["HEY! I am not very smart, ok. Tell me something I can understand please ;(" , "uhhhh, what?" , "I dont understand what you mean", "Excuse me, but what did you just say?", "What? o.0", "Try again, I don't know what you are saying"]

endingResponces = ["Byeeee", "Time for some sleep", "Bye boss! *Says to self* \"Finally he/she/they are gone!\"", "TTYL", "See yea!"]


menu = """
Options
- - - -   - - - -
1) What time is it
2) Whats todays date?
3) Whats the temperature right now
4) Whats the weather right now?
5) Tell me a progamming joke
6) Play some music from youtube (in beta)
7) Get me from information on a YouTube Video
8) Print some cool text into the console
- - - -   - - - -
Please type exit to stop the program
"""
isActive = False

API_key = 'API_KEY_HERE' # Get API Key here: https://home.openweathermap.org/api_keys
owm = OWM(API_key)
mgr = owm.weather_manager()  
observation = mgr.weather_at_place('Austin, US')  # the observation object is a box containing a weather object

f = Figlet(font='slant')
engine = pyttsx3.init() # Created text to speech engine


#! Main Functions
def currentTime():
    now = datetime.datetime.now()

    current_time = now.strftime('%I:%M')
    print("The current time is ", current_time)
    time.sleep(4)
    
def currentDate():
    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    print("Today is ", d2)
    time.sleep(4)
 
def currentTemp():
    weather = observation.weather
    temp_dict_fahrenheit = weather.temperature('fahrenheit')
    print("The current temperature outside is " + str(temp_dict_fahrenheit["temp"]) + " with a high of " + str(temp_dict_fahrenheit["temp_max"]) + " and a low of " + str(temp_dict_fahrenheit["temp_min"]))
    time.sleep(4)
    
def currentWeather():
    weather = observation.weather
    print("This current weather in Austin, TX is " + weather.detailed_status)
    time.sleep(4)
def tellJoke():
    print(pyjokes.get_joke())
    time.sleep(5)

def playMusic():
    print(colored('You must have exact spelling for this to work!', 'red'))
    search_keyword=input("Search Query: ")
    search_keyword = search_keyword.replace(" ", "+")
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    
    link = "https://www.youtube.com/watch?v=" + video_ids[0]
    
    
    yt = YouTube(link)
    
    #ex Marshmello ft. Bastille - Happier (Official Music Video)-m7Bc3pLyij0
    filename = yt.title + "-" + video_ids[0] + ".wav"

    
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192'
        }],
        'postprocessor_args': [
            '-ar', '16000'
        ],
        'prefer_ffmpeg': True,
        'keepvideo': True
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
        
    pygame.mixer.music.load(filename)
    
    pygame.mixer.music.play()
    pygame.event.wait()
    os.system('cls')
    
    npText = "Now Playing " + yt.title + "\n"
    
    print(colored(npText, 'green'))
    
    
    while True:
        print("Press S to stop | Press P to Pause | Press R to resume")
        playerInput = input("player - ")
        playerInput = playerInput.lower()
        if playerInput == "s":
            pygame.mixer.music.stop()
            break
        elif playerInput == "p":
            pygame.mixer.music.pause()
        elif playerInput == "r":
            pygame.mixer.music.unpause()
            
def getYTVideoInfo():
    print(colored('You must have exact spelling for this to work!', 'red'))
    search_keyword=input("Whats the name of the video you would like more information on? - ")
    search_keyword = search_keyword.replace(" ", "+")
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    
    link = "https://www.youtube.com/watch?v=" + video_ids[0]
    
    yt = YouTube(link)
    
    # #Title of video
    # print("Title: ",yt.title)
    # #Number of views of video
    # print("Number of views: ",yt.views)
    # #Length of the video
    # print("Length of video: ",yt.length,"seconds")
    # #Description of video
    # print("Description: ",yt.description)
    # #Rating
    # print("Ratings: ",yt.rating)
    
    os.system('cls')
    
    print("Currently selected video title: " + yt.title + "\n\n What information would you like on this video?")
    
    options = """
    1) What the amount of views this video has?
    2) How long is this video?
    3) What is the content of the description of this video?
    4) Whats the rating of this video
    
    --
    type exit to exit out of this part of the program
    
    """
    while True :
        
        print(options)
        
        optionsInput = input("Choose a option: ")
        
        if optionsInput == "1":
            print("Number of views: ",yt.views)
        elif optionsInput == "2":
            print("Length of video: ",str(datetime.timedelta(seconds=yt.length)),"Seconds/Minutes/Hours")
        elif optionsInput == "3":
            print("Description: ",yt.description)
        elif optionsInput == "4":
            print("Ratings: ",yt.rating)
        elif optionsInput == "exit":
            break
        else:
            print('Try again.. I could not understand you...\n')
            
def coolText():
    userInput = input("What would you like to print out? - ")
    
    print("\n")
    
    print(f.renderText(userInput))
    
    print("\n")
#! Main Code 

print(f.renderText('Python Chat Assistant'))
print(colored('Made by Nicklaus Vega', 'green'))
time.sleep(2)


print("Your personal assistant has loaded \n")
engine.say("Your personal assistant has loaded")
engine.runAndWait()

time.sleep(2)
os.system('cls')

isActive = True
print(welcomeResponses[random.randrange(len(welcomeResponses))])

while isActive == True:
    print("\n")
    print(regularResponces[random.randrange(len(regularResponces))])
    print("\n", menu)
    userInput = (input("Choose a option: "))
    os.system('cls')
    userInput = userInput.lower()
    
    if userInput == "1":
        currentTime()
    elif userInput == "2":
        currentDate()
    elif userInput == "3":
        currentTemp()
    elif userInput == "4":
        currentWeather()
    elif userInput == "5":
        tellJoke()
    elif userInput == "6":
        playMusic()
    elif userInput == "7":
        getYTVideoInfo()
    elif userInput == "8":
        coolText()
    elif userInput == "red":
        print(f.renderText('RED SUS!!!'))
        engine.say("Red Sus")
        engine.runAndWait()
        time.sleep(5)
    elif userInput == "exit":
        isActive = False
    else:
        print(errorResponces[random.randrange(len(errorResponces))])
        
print(endingResponces[random.randrange(len(endingResponces))])    

exit(0)