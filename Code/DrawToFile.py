__author__ = 'Davide'
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import math

def saveinfile(outputfile="output.png", points=[], maxx=1, maxy=1, xsize=2048, ysize=2048):
    app = QCoreApplication([])
    size = QSize(xsize, ysize)
    img = QImage(size, QImage.Format_RGB32)
    img.fill(QColor(255, 255, 255))

    painter = QPainter(img)
    pen = QPen(Qt.black, 2, Qt.SolidLine)
    painter.setPen(pen)

    S = min(xsize/maxx, ysize/maxy)
    Sx = maxx*S
    Sy = maxy*S
    #Offx = Sx/2-xsize/2
    #Offy = Sx/2-ysize/2
    Offx = (xsize-Sx)/2
    Offy = (ysize-Sy)/2


    for i in range(0, len(points)):
        if i+1 < len(points):
            startx = points[i][0]*S+Offx
            starty = points[i][1]*S+Offy
            endx = points[i+1][0]*S+Offx
            endy = points[i+1][1]*S+Offy
            print("x: " + str(startx) + ", y: " + str(endx))
            painter.drawLine(startx, starty, endx, endy)

    painter.end()

    img.save(outputfile)