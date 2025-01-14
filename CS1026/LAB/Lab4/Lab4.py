grade = float(input("Enter your grade: "))
if grade > 90:
    print("A+")
elif grade > 80:
    print("A")
elif grade > 70:
    print("B")
elif grade > 60:
    print("C")
elif grade > 50:
    print("D")
else:
    print("F")


div_2 = 0
div_3 = 0
div_4 = 0

for n in range(1,11):
    print(n)

    if n % 2 == 0:
        print("div by 2")
        div_2 += 1
    if n % 3 == 0:
        print("div by 3")
        div_3 += 1
    if n % 4 == 0:
        print("div by 4")
        div_4 += 1

print(str(div_2) + " numbers divisible by 2")
print(str(div_3) + " numbers divisible by 3")
print(str(div_4) + " numbers divisible by 4")

n = int(input("Enter a number: "))
all_smaller = True

for a in range(3): #can't use n, it will change the n to 0,1,2
    next_num = int(input("Enter another number: "))
    if next_num >= n: #it should be >= not <
        all_smaller = False

print(all_smaller)
