
def factorial(n):
    result = n
    for i in range(1, n):
        result = result * i

    return result

def hello_world():
    print("Hello World")

def hello_world_n_times(n):
    for i in range(n):
        hello_world()

def main():
    hello_world_n_times(2)
    hello_world_n_times(1)
    hello_world_n_times(3)
    hello_world_n_times(2)

def countVowels(word):
    numVowels = 0 #should be 0 at first not 1
    for letter in word.lower(): #not string and turn it to lower case
        if letter in "aeiou":
            numVowels += 1

    return numVowels #return numVowels not letter
