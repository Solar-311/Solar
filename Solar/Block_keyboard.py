#-*- coding: utf-8 -*-

# Imports
import ctypes
from ctypes import wintypes

BlockInput = ctypes.windll.user32.BlockInput
BlockInput.argtypes = [wintypes.BOOL]
BlockInput.restype = wintypes.BOOL

blocked = BlockInput(True)
if blocked:
    try:
        input('essaie')
    finally:
        unblocked = BlockInput(False)
else:
    raise RuntimeError('Input is already blocked by another thread!')
