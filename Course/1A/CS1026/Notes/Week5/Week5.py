
"""
st = input("Enter a String: ")
#print("Checkpoint A")
if st.find("a") != -1:
    print("Checkpoint B")
    print(st.find("a"))
    i = 0
    while st[i] != 'a':
        print("Checkpoint C")
        i = i + 1

    print("Checkpoint D")
    print("The letter after 'a' is: " + st[i+1])
else:
    print("No 'a' found.")
"""


def do_someting():
    a = "hello world"
    b = input("Enter a string: ")
    if a == b:
        print("Same")
    else:
        print("Different")


#do_someting()
#do_someting()
#do_someting()

def calculate(a,b,c):
    x = (a + b) / c
    y = b - a
    #print(a + x + y)
    return a + x + y

res = calculate(7,5,2)
print(res)
res = calculate(4,6,3)
print(res)

def work (x,y):
    s = x ** 2
    t = y ** 2
    if s > t:
        return x
    else:
        return y

def make_username ():
    fname = input("First Name: ").lower()
    lname = input("Last Name: ").lower()

    return fname[0] + get_portion(lname)

def get_portion(name):
    if len(name) > 5:
        return name[0:5]
    else:
        return name

make_username()








print("夯格睿夯格睿夯格睿夯格睿夯格睿夯格睿夯格睿夯格睿")