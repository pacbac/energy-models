def stateToIndex(state):
    stateTable = {"AZ": 0, "CA": 1, "NM": 2, "TX": 3}
    if state in stateTable:
        return stateTable[state]
    return -1
    pass

def indexToState(index):
    stateTable = {0: "AZ", 1: "CA", 2: "NM", 3: "TX"}
    if index in stateTable:
        return stateTable[index]
    return -1
    pass
