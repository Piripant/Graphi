__author__ = 'Davide'
import re
import Equator
import DrawToFile

delimiters = ["+", "-", "*", "/", "^", "(", ")"]
mchardel = ["(sin)", "(cos)", "(in)", "(log)", "(!)", "(sqrt)"]
parenthesis = ['(']


regexPattern = '|'.join(map(re.escape, delimiters))
multiPattern = '|'.join(mchardel)

formula = input("Enter formula\n")

formula = "".join(formula.split(" "))
formula = re.split('([' + regexPattern + '])|' + multiPattern, formula)

Equator.eqint(formula)
xindex = [i for i, x in enumerate(formula) if x == "x"]

points = []

maxx = 0
maxy = 0
minx = 0
miny = 0

step = 100
minvalue = 1*step
maxvalue = 100*step


for i in range(minvalue, maxvalue):
    xresult = float(i)/step
    for n in range(0, len(xindex)):
        formula[xindex[n]] = xresult

    yresult = Equator.resolve(Equator.deparenter(formula))

    if xresult > maxx:
        maxx = xresult

    if yresult > maxy:
        maxy = yresult

    if xresult < minx:
        minx = xresult

    if yresult < miny:
        miny = yresult

    points.append([])
    points[i-minvalue].append(xresult)
    points[i-minvalue].append(yresult)

print(maxx)
print(maxy)

DrawToFile.saveinfile("output.png", points, maxx-minx, maxy-miny)