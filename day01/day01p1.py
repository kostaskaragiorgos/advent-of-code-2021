n = [199,
200,
208,
210,
200,
207,
240,
269,
260,
263]



def countinc(lista):
    incretimes = 0
    for i in range(1,len(lista)):
        if lista[i] > lista[i-1]:
            incretimes += 1
    return incretimes


print(countinc(n))

with open("day01/day01p1.txt") as f:
    raw = f.read()
    input = [int(x) for x in raw.split('\n')]
    print(input)
    print(countinc(input))
