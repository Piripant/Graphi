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

    print(S)
    print(Sx)
    print(Sy)

    for i in range(0, len(points)):
        if i+1 < len(points):
            startx = -(points[i][0]*S+(xsize-Sx)/2)
            starty = -(points[i][1]*S+(xsize-Sy)/2)
            endx = -(points[i+1][0]*S+(xsize-Sx)/2)
            endy = -(points[i+1][1]*S+(xsize-Sy)/2)
            painter.drawLine(startx, starty, endx, endy)

    print(startx)
    print(starty)
    print(endx)
    print(endy)

    painter.end()

    img.save(outputfile)