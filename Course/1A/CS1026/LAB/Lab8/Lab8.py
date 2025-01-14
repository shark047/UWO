def calc(div):
    try:
        q = 12 / div
        print(q)
    except:
        print("Cannot divide by 0!")


def main():
    div = input("Enter a divisor: ")
    try:
        div = int(div)
        calc(div)
        print("Finished")
    except ValueError:
        print("Cannot convert to an int!")


main()


filename = input("Enter filename: ")

try:
    infile = open(filename, "r")
    line = infile.readline()
    value = int(line)

except FileNotFoundError:
    print("Cannot find file.")

except ValueError:
    print("Not a valid integer.")

finally:
    infile.close()

