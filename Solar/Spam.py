#-*- coding: utf-8 -*-

# Imports
import sys, os, random
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
# Image du widget
pathSpamPicture = (pathPictures + '\\wd_picture2.png')
# Icone fenêtre
pathIcon = (pathPictures + '\\Icon.ico')

# Main
class Progress (QMainWindow):

	def __init__(self):
		QWidget.__init__(self)

		# Configuration de la fenêtre
		self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint)
		self.setWindowTitle('Spam Window')
		self.setWindowIcon(QIcon(pathIcon))
		self.setStyleSheet('background-color: white;')

		# Appel des méthodes
		self.scene()
		l = random.randint(100, 1600)
		h = random.randint(50, 800)
		self.move(l, h)
		self.show()

	def scene (self):

		self.image = QPixmap(pathSpamPicture)
		self.lbl= QLabel()
		self.lbl.setPixmap(self.image)
		self.text = QLabel('Hey it s your buddy Solar :)')
		self.text.setStyleSheet('color: red; font-weight: bold')
		self.text.setFont(QFont('Consolas', 12))

		self.setCentralWidget(QGroupBox())

		self.layout = QHBoxLayout()
		self.centralWidget().setLayout(self.layout)
		self.layout.addWidget(self.lbl)
		self.layout.addWidget(self.text)

# Start
app = QApplication.instance()
if not app :
    app = QApplication(sys.argv)
p = Progress()
app.exec()
