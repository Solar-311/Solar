#-*- coding: utf-8 -*-

# Imports
import os, subprocess, sys, getpass
from pyuac import main_requires_admin

# Nom d'utilisateur actuel
username = getpass.getuser()

# Fichiers

# Directory
# Dossier Solar
pathFile = os.path.dirname(os.path.abspath(__file__))

# File
# Solar.py
pathLauncher = (pathFile + '\\Launcher.py')
# Start_Error.py
pathStart_Error = (pathFile + '\\Start_Error.py')

# Main
@main_requires_admin
def main(return_output = True):

    if os.name == 'nt'  and sys.getwindowsversion().major == 10 :
        subprocess.Popen([sys.executable, pathLauncher])
    else :
        print('Project can only run on Windows 10')
        subprocess.Popen([sys.executable, pathStart_Error])

if __name__ == "__main__":
    main()
