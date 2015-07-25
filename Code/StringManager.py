__author__ = 'Davide'
import re
import Equator
import DrawToFile

delimiters = ["+", "-", "*", "/", "^", "(", ")"]
mchardel = ["(sin)", "(cos)", "(in)", "(log)", "(!)", "(sqrt)"]
parenthesis = ['(']
regexPattern = '|'.join(map(re.escape, delimiters))
multiPattern = '|'.join(mchardel)


def splitnums(list=[]):
    list = "".join(list.split(" "))
    list = re.split('([' + regexPattern + '])|' + multiPattern, list)
    return list


def InputOuput():
    formula = input("Enter formula\ny = ")
    formula = splitnums(formula)
    Equator.eqint(formula)
    #print(formula)
    #print(Equator.resolve(Equator.deparenter(formula)))
    step = int(input("Enter steps per unit\n"))
    minvalue = step*int(input("Enter x min value\n"))
    maxvalue = step*int(input("Enter x max value\n"))

    points = []

    maxx = -maxvalue
    maxy = -maxvalue
    minx = maxvalue
    miny = maxvalue

    xindex = [i for i, x in enumerate(formula) if x == "x"]
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
        print("Point: " + str(i+1-minvalue) + "/" + str(maxvalue-minvalue) + " (" + "%.2f" %((i+1-minvalue)/(maxvalue-minvalue)*100) + "%)", end="\r")

    w = int(input("\nWrite file width: "))
    h = int(input("Write file height: "))
    filename = input("Write file name (without extension): ") + ".png"
    print("Drawing to file " + filename)
    DrawToFile.saveinfile(filename, points, maxx, minx, maxy, miny, w, h)

if __name__ == '__main__':
    InputOuput()
