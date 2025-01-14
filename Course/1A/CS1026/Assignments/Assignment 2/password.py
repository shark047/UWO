"""
************************************************
CS 1026 - Assignment 2 – Password Strength
Code by: Yiwei Dong
Student ID: ydong445
File created: October 21, 2024
************************************************
This file is used to calculate the password strength
"""


def count_groups(pwd):

    GROUP_DICT = {"lowercase": "abcdefghijklmnopqrstuvwxyz", "uppercase": "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "digits": "0123456789", "Symbols": "!@#$%^&*/?-+=,.|~"}
    #All groups dictionary

    group_found = {"lowercase": False, "uppercase": False, "digits": False, "Symbols": False}
    #count how many groups founded

    num = 0
    #count group numbers

    for letter in pwd: #check each letter in password entered
        for group_name, group_char in GROUP_DICT.items():
            if letter in group_char: #check letter in each groups
                group_found[group_name] = True

    for check in group_found.values(): #count how many groups have
        if check:
            num += 1

    return num

def password_strength(pwd):

    group_num = count_groups(pwd) #get how many groups

    if " " in pwd or "\t" in pwd or "\n" in pwd:
        return 0
    #make sure no space, \t, \n

    if len(pwd) < 5:
        return 0
    #if length is lower than 5, return 0

    elif 5 <= len(pwd) <= 8:
        if 0 <= group_num <= 1:
            return 1

        elif 2 <= group_num <= 3:
            return 2

        elif group_num == 4:
            return 3

    elif 9 <= len(pwd) <= 12:
        if 0 <= group_num <= 1:
            return 2

        elif 2 <= group_num <= 3:
            return 3

        elif group_num == 4:
            return 4


    elif len(pwd) >= 12:
        if 0 <= group_num <= 1:
            return 3

        elif 2 <= group_num <= 3:
            return 4

        elif group_num == 4:
            return 5

    #check what level is

    return 0


