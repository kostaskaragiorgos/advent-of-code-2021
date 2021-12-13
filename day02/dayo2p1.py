horip = 0
downp = 0

pos = ["forward 5",
"down 5",
"forward 8",
"up 3",
"down 8",
"forward 2"]

for i in pos:
    if i[0] == "f":
        horip += int(i[-1])
    elif i[0] == "u":
        downp -= int(i[-1])
    else:
        downp += int(i[-1])


print(horip*downp)
