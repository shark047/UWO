age = int(input("Enter your age: "))
if age >= 9:
    height = float(input("Enter your height in cm: "))
    if height > 130:
        print("You may go on this ride!")
    else:
        print("You are too short for this ride.")
else:
    print("you are too young for this ride.")





IDEAL_CREDIT_SCORE = 720

userScore = int(input("Please enter your credit score: "))
housePrice = int(input("Please enter the price of the house: "))

#if userScore => IDEAL_CREDIT_SCORE:
if userScore >= IDEAL_CREDIT_SCORE:
    downPayment = 0.1 * housePrice
#else if
elif userScore < IDEAL_CREDIT_SCORE and userScore > 600: #"600"
    downPayment = 0.2 * housePrice
else:
#downPayment = 0.3 * housePrice
    downPayment = 0.3 * housePrice

print("Your down payment is: ${}".format(downPayment))
