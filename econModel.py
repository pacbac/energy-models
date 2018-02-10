from openpyxl import load_workbook
from openpyxl import Workbook

def calcSigma(q, k , p, f):
    return (q*k)/(p*f)

def calcProportions(q, k, f, sigma):
    return f/((k**(sigma)*q**(1-sigma)))

def stateToIndex(state):
    stateTable = {"AZ": 0, "CA": 1, "NM": 2, "TX": 3}
    if state in stateTable:
        return stateTable[state]
    return -1
    pass

def main():
    wb1 = load_workbook("ProblemCData.xlsx")
    dataSheet = wb1.worksheets[0]
    msnCodes = wb1.worksheets[1]
    table = {}
    msnTable = {}

    for r in range(2, dataSheet.max_row+1):
        msn = dataSheet.cell(row=r, column=1).value #col 1
        state = stateToIndex(dataSheet.cell(row=r, column=2).value) #col 2
        yr = int(dataSheet.cell(row=r, column=3).value) #col 3
        data = float(dataSheet.cell(row=r, column=4).value) #col 4
        if msn not in table:
            table[msn] = [{}, {}, {}, {}] #0=AZ, 1=CA, 2=NM, 3=TX
        table[msn][state][yr] = data

    for r in range(2, msnCodes.max_row+1):
        msn = msnCodes.cell(row=r, column=1).value
        desc = msnCodes.cell(row=r, column=2).value
        unit = msnCodes.cell(row=r, column=3).value
        #print(desc)
        msnTable[msn] = [desc, unit] #array of [description, unit of msn]

    for i in range(0, 4):
        tc = {yr: table["TETCB"][i][yr] for yr in table["TETCD"][i].keys()}
        tap = {yr: table["TETCD"][i][yr] for yr in table["TETCD"][i].keys()}
        nrap = {yr: (table["PATCD"][i][yr]+table["NGTCD"][i][yr])/2 for yr in table["TETCD"][i].keys()}
        nrc = {yr: (table["PATCB"][i][yr]+table["NGTCB"][i][yr])/2 for yr in table["TETCD"][i].keys()}
        trc = {yr: table["RETCB"][i][yr] for yr in table["TETCD"][i].keys()}
        renewableNRGAvgPrice = {yr: float((tc[yr]*tap[yr]-nrc[yr]*nrap[yr])/trc[yr]) for yr in table["TETCD"][i].keys()}
        sigma = {yr: calcSigma(renewableNRGAvgPrice[yr], trc[yr], tap[yr], tc[yr]) for yr in table["TETCD"][i].keys()}
        proportions = {}
        for j in range(1971, 2010):
            proportions[j-1] = calcProportions(renewableNRGAvgPrice[j-1], trc[j], tc[j-1], sigma[j-1])

        print(proportions)


        wb2 = Workbook()
        wb2Sheet = wb2.active

        wb2Sheet.cell(row=1, column=1).value = "Year"
        wb2Sheet.cell(row=1, column=2).value = "A(year)"

        r = 2
        for yr in proportions.keys():
            #if key[2:5] == "TCB" and key != "LOTCB" and key != "WYTCB":
            #if key == "RFTCB" or key == "RETCB" or key =="POTCB" or key == "NGTCB" or key == "MMTCB" or key == "LGTCB" or key == "JFTCB" or key == "HYTCB" or key == "CLTCB" or key == "BMTCB":
            #if key == "RFICB" or key == "POICB" or key == "NGICB" or key == "LGICB" or key == "HYICB" or key == "CLICB":
                #print(key)
            wb2Sheet.cell(row=r, column=1).value = yr
            wb2Sheet.cell(row=r, column=2).value = proportions[yr]
            #wb2Sheet.cell(row=r, column=3).value = msnTable["TETCD"][0].replace(".", "")
            #wb2Sheet.cell(row=r, column=4).value = wb2Sheet.cell(row=r, column=4).value.replace(" total consumption", "")
            #wb2Sheet.cell(row=r, column=4).value = wb2Sheet.cell(row=r, column=4).value.replace(" total production", "")
            r += 1
        wb2.save("proportion"+str(i)+".xlsx")

    pass

if __name__ == "__main__":
    main()
