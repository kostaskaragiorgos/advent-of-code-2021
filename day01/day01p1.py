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

def triplecounter(n):
    counter = 0
    psum = 0
    sum1 = 0
    for i in range(len(n)):
        for i in range(i,i+3):
            if i+1 >= len(n):
                break
            else:
                sum1+= n[i+1]
        if sum1 > psum:
            counter+=1
        psum = sum1
        sum1 = 0
    return counter


print(countinc(n))
print(triplecounter(n))

with open("day01/day01p1.txt") as f:
    raw = f.read()
    input = [int(x) for x in raw.split('\n')]
    print(input)
    print(countinc(input))
    print(triplecounter(input))
