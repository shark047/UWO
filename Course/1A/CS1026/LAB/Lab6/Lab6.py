#activity 1
unique_numbers = []

while len(unique_numbers) < 10:
    user_input = input("Please enter a unique number: ")

    if user_input.isdigit():
        number = int(user_input)

        if number not in unique_numbers:
            unique_numbers.append(number)
            print(number, "already append to the list")
        else:
            print(number, "already in the list, please enter other number.")

    else:
        print("Please enter a vaild number.")

print(unique_numbers)

#activity 2
def count_matching_strings(strings):
    count = 0

    for word in strings:
        if len(word) >= 3 and word[0] == word[-1]:
            count += 1
    return count

strings = ['bgh', 'yuy', 'aa', 'wer', '1661']
print("Number of matching strings:", count_matching_strings(strings))

#activity 3
def make_dict(groceries):

    groc_dict = {}

    for item in groceries:

        first_letter = item[0].lower()

        if first_letter not in groc_dict:
            groc_dict[first_letter] = [item]
        else:
            groc_dict[first_letter].append(item)

    return groc_dict

groceries = ["salami", "cucumber", "cheese", "milk", "salsa"]
print(make_dict(groceries))

#part 2-1
def z_first_sort(words):
    zresult = []
    result = []
    
    for word in words:
        if word.lower()[0] == "z":
            zresult.append(word)
        else:
            result.append(word)
    
    zresult.sort()
    result.sort()
    
    return zresult + result

#part 2-2
values = [1,2,3,4,5] 
newValues = list(values) #newValues = values will make they change together
for i in range(len(values)):  #it shouldn't +1
    newValues[i] +=1 #it should be newvalues not values
    print("Old Value at index {} is: {} ".format(i, values[i])) #old value should be values list not newvalues list
    print("New Value at index {} is: {} \n".format(i, newValues[i])) 