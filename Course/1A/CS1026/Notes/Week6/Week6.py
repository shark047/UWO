
def my_function(x, y):
    num = int(input("Enter a number: "))
    if x > num or y > num:
        print("Hello")
        return "Hello"
    elif num > x and num > y:
        print("Hi")
        return "Hi"

#my_function(4,7)
#res = my_function(4,7)
#print(res)


def calculate(a, b, c = 5):
    return a + b + c

#print(calculate(2,6,3))
#print(calculate(2, 4))


def get_user_input(n):
    nums = []
    for i in range(n):
        num = int(input("Enter a number: "))
        nums.append(num)
    return nums

def calc_avg(x):
    total = 0
    num = 0
    for v in x:
        total += v
        num += 1
    res = total / num
    return res

def calc_min(x):
    small = x[0]
    for v in x:
        if v < small:
            small = v
    return small

def main():
    data = get_user_input(5)

    avg = calc_avg(data)
    print("Average: ", avg)

    min = calc_min(data)
    print("Min: ", min)

#main()

nums = [0] * 10
print(nums)

nums = [[0]] * 10
nums[0].append(5)
print(nums)

alist = ["apple", "mango", "orange"]
blist = alist
blist = alist[:]
blist = list(alist)
blist.append("watermelon")
#print(alist)
#print(blist)

#alist.append(blist)
#print(alist)

a = [3, 5, 2]
b = [4, 8 , 1]

print(a + b)


diction = {'a': 5, 'b': 9, 'c': 2, 'd': 6}
print(diction['a'])
diction['c'] = 7
print(diction)


for k in diction.keys():
    print(k)

for v in diction.values():
    print(v)

for p in diction.items():
    print(p)

for k in diction.keys():
    print(k, "=>", diction[k])


nums = [15, 74, 149, 93, 52402, 1900, 9273, 7]

num_dict = {}

for num in nums:
    fdig = str(num)[0]
    print(fdig)
    if fdig in num_dict.keys(): #检测第一个数字，按第一个数字归类
        #already a key
        num_dict[fdig].append(num)

    else:
        #not yet a key
        num_dict[fdig] = [num]
        #创建为list，上面可以append

print(num_dict)
#output {'1': [15, 149, 1900], '7': [74, 7], '9': [93, 9273], '5': [52402]}

#Tuples
tup = (2, 7, 6, 9)
print(tup)
tup[1] = 3

