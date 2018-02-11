import econModel
from econModel import *
from rungeKutta import *
from realGDP import *

competeDict = {}
stateNum = 0

ourKeys = ["RFTCB", "RETCB", "POTCB", "NGTCB", "MMTCB", "LGTCB", "JFTCB", "HYTCB", "CLTCB", "BMTCB"]
renewable = [False, True, False, False, False, False, False, True, False, True]

def load():
    for key in ourKeys:
        if key not in competeDict:
            competeDict[key] = {yr: table[key][stateNum][yr] for yr in table["GDPRX"][stateNum].keys()}

def main():
    global stateNum
    global table
    startYear = 1986 #1978 <= year <= 2009
    endYear = 1988
    startN = {}
    for state in range(0, 4):
        for key in ourKeys: #set up N(t = start)
            startN[key] = table[key][state][startYear]
        totalRenewable = 0
        totalNonRenewable = 0
        for i in range(0, len(ourKeys)):
            c = Coord(startYear, table[ourKeys[i]][state][startYear])
            if renewable[i]:
                totalRenewable += approx(startYear, endYear, c, 1, startYear, ourKeys[i])
            else:
                totalNonRenewable += approx(startYear, endYear, c, 1, startYear, ourKeys[i])
        currentTConsump =
        print(state, total)

    #print(avgApproxX, approx(0, 1, Coord(avgApproxX, table["BMTCB"][0][avgApproxX]), 1, avgApproxX).y)

    #avgApproxY += 0.04*(approx(2, 3, Coord(1974, table["BMTCB"][0][1974]), 1, 1974).y)


    #print(avgApproxX, avgApproxY)
    pass

load()
if __name__ == "__main__":
    main()
