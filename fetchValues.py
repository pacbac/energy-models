from openpyxl import load_workbook
from openpyxl import Workbook

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

    wb2 = Workbook()
    wb2Sheet = wb2.active

    wb2Sheet.cell(row=1, column=1).value = "MSN"
    wb2Sheet.cell(row=1, column=2).value = "Year"
    wb2Sheet.cell(row=1, column=3).value = "Data"
    wb2Sheet.cell(row=1, column=4).value = "Description"
    """Find corresponding keys in the sheet"""
    r = 2
    for key in table.keys():
        #if key[2:5] == "TCB" and key != "LOTCB" and key != "WYTCB":
        if key == "RFTCB" or key == "RETCB" or key =="POTCB" or key == "NGTCB" or key == "MMTCB" or key == "LGTCB" or key == "JFTCB" or key == "HYTCB" or key == "CLTCB" or key == "BMTCB":
        #if key == "RFICB" or key == "POICB" or key == "NGICB" or key == "LGICB" or key == "HYICB" or key == "CLICB":
            #print(key)
            for yr in table[key][3]:
                wb2Sheet.cell(row=r, column=1).value = key
                wb2Sheet.cell(row=r, column=2).value = yr
                wb2Sheet.cell(row=r, column=3).value = table[key][3][yr]
                wb2Sheet.cell(row=r, column=4).value = msnTable[key][0].replace(".", "")
                wb2Sheet.cell(row=r, column=4).value = wb2Sheet.cell(row=r, column=4).value.replace(" total consumption", "")
                wb2Sheet.cell(row=r, column=4).value = wb2Sheet.cell(row=r, column=4).value.replace(" total production", "")
                r += 1
    wb2.save("totalConsumptionTX.xlsx")
    pass

if __name__ == "__main__":
    main()
