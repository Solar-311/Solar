#-*- coding: utf-8 -*-

# Imports
import sys, os
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
pathBackground = (pathPictures + '\\sad.jpg')
# Icone fenêtre
pathIcon = (pathPictures + '\\Icon.ico')

# Main
class Progress (QMainWindow):

	def __init__(self):
		QWidget.__init__(self)

		# Configuration de la fenêtre
		self.setWindowFlags(self.windowFlags() & ~ Qt.WindowMaximizeButtonHint)
		self.setWindowTitle('Start_Error')
		self.setWindowIcon(QIcon(pathIcon))
		self.setStyleSheet('background-color: black;')

		# Appel des méthodes
		self.scene()
		self.show()
		self.move(250, 80)

	def scene (self):

		self.pixmap = QPixmap(pathBackground)
		self.lbl= QLabel()
		self.lbl.setPixmap(self.pixmap)

		self.setCentralWidget(QGroupBox())

		self.layout = QHBoxLayout()
		self.centralWidget().setLayout(self.layout)
		self.layout.addWidget(self.lbl)

# Start
app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)
p = Progress()
app.exec()
