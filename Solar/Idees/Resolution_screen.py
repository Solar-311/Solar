import win32api
import win32con
import pywintypes

devmode = pywintypes.DEVMODEType()

devmode.PelsWidth = 1
devmode.PelsHeight = 1

devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT

win32api.ChangeDisplaySettings(devmode, 0)

# Reviens à l'ancienne résolution
win32api.ChangeDisplaySettings(None, 0)
