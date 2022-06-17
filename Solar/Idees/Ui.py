#-*- coding: utf-8 -*-

# ----- Imports -----

import sys, os, random
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# ----- Fichiers necessaires -----

pathFile = os.path.dirname(os.path.abspath(__file__))
pathPictures = str(pathFile + '\\Pictures')
pathIcon = str(pathPictures + '\\Icon.ico')
pathWallpaper = str(pathPictures + '\\Wallpaper.jpg')

# ----- Main -----

COLUMN_WIDTH = 5
DELTA = 5

def elements() :

    delta = 10
    pixmap = QPixmap(1920, 1080)
    pixmap.fill(QColor('black'))
    painter = QPainter(pixmap)

    for i in range(5, 10):

        dt = i * delta
        r = QRect(pixmap.rect().adjusted(0, dt, 0, -dt))
        color = QColor(255, 0, 0)
        painter.fillRect(r, color)
    painter.end()

    return pixmap

def apply_effect(pixmap, number_of_columns):

    i = round(pixmap.width() / COLUMN_WIDTH)

    for _ in range(number_of_columns):
        j = random.randint(0, i)
        rect = QRect(j * COLUMN_WIDTH, 0, COLUMN_WIDTH, pixmap.height())
        pix = pixmap.copy(rect)
        painter = QPainter(pixmap)
        painter.drawPixmap(rect.translated(0, DELTA), pix)
    painter.end()

    return pixmap

# ----- Launcher -----

def main_ui () :

    # Config de l'appli
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(pathIcon))

    pixmap_demo = elements()
    label = QLabel(pixmap=pixmap_demo)
    label.setWindowTitle('Solar')
    label.showFullScreen()

    def on_timeout () :

        out_pixmap = apply_effect(label.pixmap(), 90)
        label.setPixmap(out_pixmap)

    timer = QTimer(interval=0.1, timeout=on_timeout)
    timer.start()
    app.exec_()
main_ui()