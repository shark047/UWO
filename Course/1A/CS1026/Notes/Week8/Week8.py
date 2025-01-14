

"""
file = open("countrys.txt", "r")

t = 0

for line in file:
    line = line.strip()
    line = line.rsplit(" ", 1)

    t += int(line[1])

    print(line)


file.close()

file = open("data.txt", "r")

t = 0

for line in file:
    line = line.strip()
    line = line.split("-")

    print(line)

    t += int(line[0])
    print(t)


file.close()
"""

#x = "a" + 5 # type error

x = []
# print(x[2]) # Index error

#x = 5 / 0 # ZeroDivisionError

#print("hello world")

try:
    x = 5 / 0
    print("hi")

except ZeroDivisionError:
    print("caught error")

print("hello world")





try:
    x = "a" + 5
    print("hi")

except TypeError:
    print("caught error")

print("hello world")



try:
    fname = input("Enter the file name:")
    file = open(fname, "r")

    for line in file:
        line = line.strip()
        line = line.strip("!*")
        line = line.split("-")
        print(line[3])

except FileNotFoundError:
    print("This file doesn't exist")
except:
    print("an error occurred")

finally:
    file.close()


num = int(input("Enter a number:"))


