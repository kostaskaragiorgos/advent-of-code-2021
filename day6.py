
with open("day6.txt") as f:
    initst =f.read()
    initst = initst.split(",")
    initst = [int(inits) for inits in initst]

def fishcounter(initstate, days):
    for _ in range(days):
        for i in range(len(initstate)):
            if initstate[i] == 0:
                initstate[i] = 6
                initstate.append(8)
            else:
                initstate[i] -= 1
    return initstate



print(len(fishcounter(initst, 80)))