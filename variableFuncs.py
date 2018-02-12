import math

def calcProportion(yr, state):
    stateTable = {0: calcProportionAZ, 1: calcProportionCA, 2: calcProportionNM, 3: calcProportionTX}
    return stateTable[state](yr)

def calcProportionTX(yr):
    #return yr/1000
    return 77.49*math.sin(0.09199*yr-17.88)+70.81*math.sin(0.09832*yr+136.1)

def calcProportionNM(yr):
    return 62.72*math.sin(0.07689*yr+12.56)+56.69*math.sin(0.0808*yr+165.3)

def calcProportionCA(yr):
    return 769*math.sin(0.0006886*yr+163.6)+0.08925*math.sin(0.2558*yr-178.5)

def calcProportionAZ(yr):
    return 85.58*math.sin(0.05192*yr+62.53)+82.07*math.sin(0.05366*yr+225.6)

def calcTotalAvgPrice(yr, state):
    stateTable = {0: [82.65, 0.1166, -36.49, 71.56, 0.1319, 130.9], 1: [57.62, 0.1181, -39.53, 48.25, 0.14, 114.9], 2: [67.13, 0.1166, -36.66, 58.02, 0.1343, 126], 3: [54.22, 0.1187, -40.7, 47.73, 0.1384, 118]}
    consts = stateTable[state]
    return consts[0]*math.sin(consts[1]*yr+consts[2]) + consts[3]*math.sin(consts[4]*yr+consts[5])
    #return (3.803*10**-30)*math.exp(0.0352*yr)
    #return (1.453*10**-35)*math.exp(0.0414*yr)
    #return (1.491*10**-33)*math.exp(0.03906*yr)

def calcNonRenewableAvgPrice(yr, state):
    stateTable = {0: [42.28, 0.1191, -41.53, 35.89, 0.1405, 113.8], 1: [36.39, 0.1162, -35.7, 30.42, 0.1412, 112.4], 2: [42.53, 0.1196, -42.45, 36.76, 0.1407, 113.3], 3: [32.04, 0.1153, -34.01, 27.55, 0.1394, 115.8]}
    consts = stateTable[state]
    return consts[0]*math.sin(consts[1]*yr+consts[2]) + consts[3]*math.sin(consts[4]*yr+consts[5])
    #return (1.713*10**-35)*math.exp(0.04114*yr)
