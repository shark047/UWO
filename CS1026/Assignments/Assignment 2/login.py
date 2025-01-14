"""
************************************************
CS 1026 - Assignment 2 – Password Strength
Code by: Yiwei Dong
Student ID: ydong445
File created: October 21, 2024
************************************************
This file is used to allow users create password or generate random password until the password strength is over min strength
"""




from password import *
from generate import *

def process_password(min_strength):

    while True:

        user_input = input("Type in a new password or type X for a randomly generated password: ")
        #get user's password

        if user_input.lower() == "x":

            pwd = generate_password(15) #create a password by use generate function
            pwd_strength = password_strength(pwd) #test the password strength

            print("Your password is", pwd)
            print("Your password has a strength of", pwd_strength)
            print("Your password is strong enough! Thank you.")
            #output
            break

        else: #if user use their own password
            pwd_strength = password_strength(user_input)
            #check password strength

            print("You entered:", user_input)
            print("Your password has a strength of", pwd_strength)

            if pwd_strength >= min_strength: #check if the password is available then break, if not, continue
                print("The password is strong enough! Thank you.")
                break
            elif pwd_strength < min_strength:
                print("Your passport is not strong enough. Please create a new password that is stronger.")

