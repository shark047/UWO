

"""
x = []

for i in range(5, 30,5):
    x.append(i)

for j in range(10, 5, -1):
    x.insert(0,j)

print(x)

food = ["pasta", "steak", "rice", "veggies", "chicken"]
food.append("salad")

count = 0
for f in food:
    if len(f) == 5:
        count += 1

print(food)
print(count)

food_dict = {}
for f in food:
    n = len(f)
    if n in food_dict:
        food_dict[n].append(f)
    else:
        food_dict[n] = [f]

print(food_dict)

alist = [7, 3, 1, 6]

blist = alist
#改其中一个另外一个也会改

blist = list(alist)
blist = alist[:]
#俩独立的

blist[0] = 8
alist.append(9)

print(alist)
print(blist)
"""

file = open("test1.txt", "r")

for line in file:
    line = line.strip()
    line = line.split(",")

    print(line)

file.close()

file = open("test2.txt", "r")
newfile = open("avg.txt", "w")

for line in file:
    line = line.strip()
    line = line.split(",")
    avg = (int(line[1]) + int(line[2]) + int(line[3])) / 3.0
    print(line[0],avg)
    newfile.write(line[0] + ": " + str(round(avg,2)) + "\n")

    print(line)

file.close()