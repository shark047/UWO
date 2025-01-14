import math

x = math.sqrt(3) ** 2
print(x)

print(abs(3-x))
#if x == 3.0:#does not work!
if abs(3-x) < 0.001:
    print("x is 3")
else:
    print("x is not 3")


k = 35
if k < 20:
    print("A")
elif k < 30:
    print("B")
elif k < 40:
    print("C")
elif k < 50:
    print("D")

k = 35
if k < 20:
    print("A")
if k < 30:
    print("B")
if k < 40:
    print("C")
if k < 50:
    print("D")

a = 15
b = 7
c = 11

if a > abs(b-c):
    if c > a or b < a:
        print("Hello")
    if b % 2 == 0 or c > b:
        print("Hi")
else:
    print("Goodbye")


if a < b or a < c:
    if b > c:
        print("HI")
else:
    print("Goodbye")

if a > b and a > c:
    print("Aloha")

