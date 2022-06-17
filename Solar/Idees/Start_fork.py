#-*- coding: utf-8 -*-

# Imports
import threading, subprocess, sys, os, time

# Fichiers

# Directory
# Dossier Solar
pathFile = os.path.dirname(os.path.abspath(__file__))

# File
# Fork.bat
pathFork = (pathFile + '\\Fork.bat')

# Main
def start_fork ():
    time.sleep(15)
    subprocess.call(pathFork)

thread = threading.Thread(target=start_fork)
thread.daemon = True
thread.start()
