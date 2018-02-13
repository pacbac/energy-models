import math

def calcProportion(yr, state):
    if state == 0:
        return (5.895*yr**3-1.152*10**4*yr**2-11.6*yr+0.3257)/(yr**3-1942*yr**2-9.761*yr+0.4143)
    elif state == 1:
        return (3.792*yr**2+0.1939*yr+0.01028)/(yr**2+0.057*yr+0.002798)
    elif state == 2:
        return (0.1602*yr**2+184*yr+0.7188)/(yr**2-1908*yr-0.6452)
    return (2.073*10**7)*math.exp(-0.007473*yr)

def calcNonRenewableAvgPrice(yr, state):
    if state == 0:
        return (54.16*yr**3-(1.066*10**5)*yr**2-104.5*yr+0.5053)/(yr**3-1817*yr**2+1201*yr+1.932)
    elif state == 1:
        return (75.46*yr**3-(1.485*10**5)*yr**2-145.4*yr+0.2596)/(yr**3-1745*yr**2+2316*yr+2.907)
    elif state == 2:
        return (73.25*yr**3-(1.442*10**5)*yr**2-140.6*yr+0.3808)/(yr**3-1747*yr**2+2181*yr+2.274)
    return (79.01*yr**3-(1.556*10**5)*yr**2-150.7*yr+0.3015)/(yr**3-1674*yr**2+2503*yr+3.245)

def calcRenewableAvgPrice(yr, state):
    if state == 0:
        return (782.1*yr**3-1.545*10**6*yr**2-1529*yr-1.098)/(yr**3-1972*yr**2+(2.569*10**5)*yr+257.3)
    elif state == 1:
        return (201.1*yr**3-3.963*10**5*yr**2-395.8*yr+0.1043)/(yr**3-1925*yr**2+1.401*10**4*yr+14.2)
    elif state == 2:
        return (790.9*yr**3-1.561*10**6*yr**2-1567*yr-0.9296)/(yr**3-2051*yr**2+2.179*10**5*yr+219.2)
    return (1045*yr**3-2.052*10**6*yr**2-2048*yr-1.434)/(yr**3-2113*yr**2+4.43*10**5*yr+443)

def calcPTotal(yr, state, bigQ, F):
    return calcRenewableAvgPrice(yr, state)*(bigQ/F)+calcNonRenewableAvgPrice(yr, state)*(1-(bigQ/F))
