"""

k = 0
for i in range(5):
    for j in range(3):
        k += 1
        print(i,j)

print(k)

k = 0

for i in range(5):
    k += 1
for j in range(3):
    k += 1
print(k)

"""


p = 5
q = 3
r = 9

while p > q:
    x  = 0
    while x < r:
        x += 2
        p = r
        q += 1

print(p,q,r)

"""

# option 1
num = 1
while num > 0:
    num = int(input("Enter a number: "))
    print(num)
print("Done.")

# option 2
num = int(input("Enter a number: "))
while num > 0:
    print(num)
    num = int(input("Enter a number: "))
print("Done.")




food = input("Type a food: ")
while food != 'q':
    print("I like " + food)
    food = input("Type a food: ")
   


num = ""
while not(num.isnumeric()) or int(num) <= 0:
#while int(num) <= 0 or not(num.isnumeric()): #Notice the order makes a BIG difference
    num = input("Enter a positive value: ")



print("You entered: " + num)

"""

#name error
#print(hello)

#Index Error
#s = "Western"
#print(s[12])

#Type Error
#s = "abc" + 123
#print(s)

#Value Error
#s = int("abc")
#print(s)

#x = 1
#print(x.isdigit()) 要加上str()

#syntax Error
#s = "Hello

#Zero Division Error
#x = 0
#print(20 / x)

#Infinite loop
#t = 0
#while t < 10:
    #print(t)
#    k = t * 4







