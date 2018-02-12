from competeResources import competeDict, stateNum, ourKeys
from econModel import *

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x) + " " + str(self.y)

def dn(c, yr, carryingCapacity, keyI, nList, sigma):
    interSpecies = 0 #interSpecies competition
    for key in nList.keys():
        if key != keyI:
            interSpecies += float(1/carryingCapacity)*nList[key]
    return sigma*c.y*(1-interSpecies)

def k1(h, c, yr, carryingCapacity, keyI, nList, sigma):
    return h*dn(c, yr, carryingCapacity, keyI, nList, sigma)

def k2(h, c, yr, carryingCapacity, keyI, nList, sigma):
    return h*dn(Coord(c.x+h/2, c.y+k1(h, c, yr, carryingCapacity, keyI, nList, sigma)/2), yr, carryingCapacity, keyI, nList, sigma)

def k3(h, c, yr, carryingCapacity, keyI, nList, sigma):
    return h*dn(Coord(c.x+h/2, c.y+k2(h, c, yr, carryingCapacity, keyI, nList, sigma)/2), yr, carryingCapacity, keyI, nList, sigma)

def k4(h, c, yr, carryingCapacity, keyI, nList, sigma):
    return h*dn(Coord(c.x+h/2, c.y+k3(h, c, yr, carryingCapacity, keyI, nList, sigma)), yr, carryingCapacity, keyI, nList, sigma)

def approx(index, maxIndex, c, h, yr, carryingCapacity, keyI, nList, sigma): #keyI is the key that matches so that dn will not overlap keys
    if index == maxIndex:
        return c
    next = Coord(c.x+h, c.y+float(1/6)*(k1(h, c, yr, carryingCapacity, keyI, nList, sigma)+2*k2(h, c, yr, carryingCapacity, keyI, nList, sigma)+2*k3(h, c, yr, carryingCapacity, keyI, nList, sigma)+k4(h, c, yr, carryingCapacity, keyI, nList, sigma)))
    return approx(index+1, maxIndex, next, h, yr, carryingCapacity, keyI, nList, sigma) #returns a coord
