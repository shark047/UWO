"""
st = "Western University"

print(st[4])
print(st[0:4]) # start at 0, end at index 3 (not 4)
print(st[:6]) #start at 0, end at index 5
print(st[9:]) #start at 9, end at very end of string
print(st[-1]) #-1 means last character
print(st[-3]) # 3rd last character

print(st[2] + st[8].lower() + st[6] + st[6] + st[-1])

st2 = st.replace("e", "a")
print(st)
print(st2)
st2 = st2.replace("s", "p")
print(st2)

res = st.find("t")
print(res) #第一个t的位置
res = st.find("d")
print(res) # -1 代表找不到
res = st.count("s")
print(res) #总共有几个s
res = st.find("e", 5)
print(res) #寻找从5之后的第一个e的位置

"""

"""
a = 10
b = 3
c = 16
print(a > b and a > c)
print(a > b or a > c)
print(a > b and c > b)
print(b < a < c)
print(b**2 + c == a*2)

"""

"""
s = "Hello"
t = "Hi"
print(s == t)
u = "hello"
print(s == u)
print(s.lower() == u.lower())
print(s < t)
print(s < u) #排序：A-Z < a-z
print(s)
print(t)
print("Z" < "a")

"""

a = 5
b = 4
c = 8

if a < b:
    print("A")
elif a < c:
    print("B")
else:
    print("C")

if a < b:
    if a < c:
        print(a)
    else:
        print(c)
else:
    print(b)

s = "Hello"
t = "hi"
if s == t:
     print("equal")
elif s.upper() == t.upper():
    print("same upper")
elif s.lower() != t.lower():
    if not(s == "Hi"):
        print("YES")
    else:
        print("same lower")
        print("Where am I?")
else:
    print("different")

x = 5
print(not(not(not(not(not(not(not(not(x == 10)))))))))

