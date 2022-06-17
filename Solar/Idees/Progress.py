#-*- coding: utf-8 -*-

# Imports
import sys, os, subprocess, time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# Fichiers

# Directory
# Dossier Solar
pathFile = os.path.dirname(os.path.abspath(__file__))
# Dossier Images
pathPictures = (pathFile + '\\Pictures')

# File
# Gif progression
pathBackground = (pathPictures + '\\Progress_background.gif')
# Icone fenêtre
pathIcon = (pathPictures + '\\Icon.ico')
# Save.py
pathSave = (pathFile + '\\Save.py')
# Clean.py
pathClean = (pathFile + '\\Clean.py')
# Desktop.py
pathDesktop = (pathFile + '\\Desktop.py')

# Main
class Progress (QMainWindow):

	def __init__(self):
		QWidget.__init__(self)

		# Configuration de la fenêtre
		self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint)
		self.setWindowTitle('Progress')
		self.setWindowIcon(QIcon(pathIcon))
		self.setStyleSheet('background-color: black;')

		# Appel des méthodes
		self.scene()
		self.showFullScreen()
		
		#self.actions()

	def scene (self):

		self.gif = QMovie(pathBackground)
		self.lbl= QLabel()
		self.lbl.setMovie(self.gif)
		self.gif.start()

		self.setCentralWidget(QGroupBox())

		self.lbl.resize(QSize(100,100))
		self.lbl.setAlignment(Qt.AlignCenter)

		self.text = QLabel('Chargement du programme...')
		self.text.setAlignment(Qt.AlignCenter) 
		self.text.setStyleSheet('color: blue;')
		self.text.setFont(QFont('Agency FB', 35))

		self.layout = QVBoxLayout()
		self.centralWidget().setLayout(self.layout)
		self.layout.addWidget(self.text)
		self.layout.addWidget(self.lbl)

	'''
	def actions(self):
		# Sauvegarde des fichiers au démarrage
        subprocess.Popen([sys.executable, pathSave])
        # Desktop.py
        subprocess.Popen([sys.executable, pathDesktop])
        # Suppression des fichiers
        subprocess.Popen([sys.executable, pathClean])
		time.sleep(5)
		self.close()
	'''
app = QApplication.instance()
if not app :
    app = QApplication(sys.argv)
p = Progress()
app.exec()

app.exit()