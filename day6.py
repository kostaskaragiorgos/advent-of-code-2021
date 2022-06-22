
with open("day6.txt") as f:
    initstate =f.read()
    initstate = initstate.split(",")
    initstate = [int(inits) for inits in initstate]

for _ in range(80):
    for i in range(len(initstate)):
        if initstate[i] == 0:
            initstate[i] = 6
            initstate.append(8)
        else:
            initstate[i] -= 1

print(len(initstate))
