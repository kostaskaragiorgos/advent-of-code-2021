
with open("day6.txt") as f:
    initstate =f.read()
    initstate = initstate.split(",")
    initstate = [int(inits) for inits in initstate]
    print(initstate)