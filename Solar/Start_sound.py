#-*- coding: utf-8 -*-

# Imports
import threading, os, sys
from playsound import playsound

# Main

pathFile = os.path.dirname(os.path.abspath(__file__))
wavFile = (pathFile + '\\Sounds\\chupapi.wav')

def start_sound ():

    playsound(wavFile)

thread_sound = threading.Thread(target=start_sound)
thread_sound.start()
