from cv2 import line


with open('day3.txt', 'r') as f:
    lines = f.readlines()
    lines = [entry.strip() for entry in lines]


epsilonrates = ""
gamarates = ""
for i in range(len(lines[0])):

    ents = [ent[i] for ent in lines]
    if ents.count('1') > len(lines)/2:
        epsilonrates += "1"
        gamarates += "0"
    else:
        epsilonrates += "0"
        gamarates += "1"



print(int(epsilonrates,2)  * int(gamarates, 2))



    
    

