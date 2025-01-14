done = False

while not(done):

    file = input("Enter a file name: ")

    try:
        file = open(file, "r")


        data = file.read()
        print(data)



        file.close()

        done = True

    except FileNotFoundError:
        print("File doesn't exist.")


rfile = input("Enter a file to read: ")

wfile = input("Enter a file to write to: ")

rfile = open(rfile, "r")

wfile = open(wfile, "w")


try:
    testfile = open(wfile, "r")
    testfile.close()

except:
    print("This wfil does not exist... so we can use it!")

    