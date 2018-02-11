import competeResources
from competeResources import competeDict, stateNum, ourKeys, renewable
import econModel
from econModel import *

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x) + " " + str(self.y)

def dn(c, yr, keyI):
    interSpecies = 0 #interSpecies competition
    for key in competeDict.keys():
        if key != keyI:
            carryingCapacity = table["TETCB"][stateNum][yr-1]
            interSpecies += float(1/carryingCapacity)*competeDict[key][yr]
    return sigma[yr]*c.y*(1-interSpecies)

def k1(h, c, yr, keyI):
    return h*dn(c, yr, keyI)

def k2(h, c, yr, keyI):
    return h*dn(Coord(c.x+h/2, c.y+k1(h, c, yr)/2), yr, keyI)

def k3(h, c, yr, keyI):
    return h*dn(Coord(c.x+h/2, c.y+k2(h, c, yr)/2), yr, keyI)

def k4(h, c, yr, keyI):
    return h*dn(Coord(c.x+h/2, c.y+k3(h, c, yr)), yr, keyI)

def approx(index, maxIndex, c, h, yr, keyI): #keyI is the key that matches so that dn will not overlap keys
    if index == maxIndex:
        return c
    next = Coord(c.x+h, c.y+float(1/6)*(k1(h, c, yr, keyI)+2*k2(h, c, yr, keyI)+2*k3(h, c, yr, keyI)+k4(h, c, yr, keyI)))
    return approx(index+1, maxIndex, next, h, yr, keyI) #returns a coord
