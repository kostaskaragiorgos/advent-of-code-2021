

pos = ["forward 5",
"down 5",
"forward 8",
"up 3",
"down 8",
"forward 2"]


def finddepth(lista):
    horip = 0
    downp = 0
    for i in lista:
        if i[0] == "f":
            horip += int(i[-1])
        elif i[0] == "u":
            downp -= int(i[-1])
        else:
            downp += int(i[-1])
    return horip*downp


with open("day02/day02p1.txt") as f:
    raw = f.read()
    input = [x for x in raw.split('\n')]
    print(finddepth(input))