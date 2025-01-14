"""
st = "Welcome to Western"

for ch in st[4:12]:
    #print(ch, end = " ")
    if ch == 'W' or ch == 'e':
        print(ch)
"""
st = "I love programming!"
#option 1
if 'a' in st:
    print("1. It exists in st.")
#option 2
if st.find('a') >= 0:
    print("2. It exists in st.")
#option 3
flag = False
for ch in st:
    if ch == 'a':
        flag = True

if flag == True: #if flag
    print("3. It exists in st.")
else:
    print("3. It does not exist.")

#check if string is composed only of 'a's

st = "aaaAa"
flag = True
for ch in st:
    if ch.lower() != 'a':
        flag = False

if flag:
    print("It is all 'a's")
else:
    print("Not all 'a's")


t = 0
while t < 5:
    t = t + 1
    #print(t)

t = 0
while t < 20:
    t = t + 3
    #print(t)

t = 10
while t > 0:
    t = t - 1
    #print(t)

t = 1
while t < 80:
    t = t * 2
    #print(t)




