__author__ = 'Davide'
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import math

def saveinfile(outputfile="output.png", points=[], maxx=1, minx=1, maxy=1, miny=1, xsize=4096, ysize=4096):
    app = QCoreApplication([])
    size = QSize(xsize, ysize)
    img = QImage(size, QImage.Format_RGB32)
    img.fill(QColor(255, 255, 255))

    painter = QPainter(img)
    pen = QPen(Qt.black, 2, Qt.SolidLine)
    painter.setPen(pen)
    
    gsizex = maxx-minx
    gsizey = maxy-miny
    
    S = min(xsize/gsizex, ysize/gsizey)
    Sx = gsizex*S
    Sy = gsizey*S
    Offx = (xsize-Sx)/2
    Offy = (ysize-Sy)/2


    for i in range(0, len(points)):
        if i+1 < len(points):
            startx = (points[i][0]-minx)*S+Offx
            starty = (points[i][1]-miny)*S+Offy
            endx = (points[i+1][0]-minx)*S+Offx
            endy = (points[i+1][1]-miny)*S+Offy
            painter.drawLine(startx, starty, endx, endy)

    painter.end()

    img.save(outputfile)
