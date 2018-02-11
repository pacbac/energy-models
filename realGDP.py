def cpiFunc(state, cpi):
    funcTable = {0: cpiAZ, 1: cpiCA, 2: cpiNM, 3: cpiTX}
    if state in funcTable:
        return funcTable[state](cpi)
    return

def cpiAZ(cpi):
    return (-6.602*10**6)*cpi**(-0.2956)+(2.863*10**6)

def cpiCA(cpi):
    return 4967*cpi**1.181+(5.574*10**6)

def cpiNM(cpi):
    return (1.747*10**6)*cpi**0.1301-(2.327*10**6)

def cpiTX(cpi):
    return 8636*cpi**1.246+(7.58*10**6)
