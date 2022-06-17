#-*- coding: utf-8 -*-

# Imports
import os, getpass, shutil, ctypes, sys

# Fichiers

# Directory
# Dossier Solar
pathFile = os.path.dirname(os.path.abspath(__file__))
# Dossier Images
pathPictures = (pathFile + '\\Pictures')

# File
# Fond d'écran
pathWallpaper = (pathPictures + '\\Wallpaper.jpg')

# Main
class Desktop:

	def set_wallpaper (self):

		SPI_SETDESKWALLPAPER = 0x0014
		SPIF_UPDATEINIFILE   = 0x2 # Force l'actualisation instantané
		ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, pathWallpaper ,SPIF_UPDATEINIFILE)

		if ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, pathWallpaper ,SPIF_UPDATEINIFILE) == True :
			print('Le fond d écran a été appliqué avec succès')
		else :
			print('Erreur lors du chargement du fond d écran\n'
				'Dans : Desktop.py/set_wallpaper')

Desktop().set_wallpaper()
