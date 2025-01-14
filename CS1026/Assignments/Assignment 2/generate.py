"""
************************************************
CS 1026 - Assignment 2 – Password Strength
Code by: Yiwei Dong
Student ID: ydong445
File created: October 21, 2024
************************************************
This file is used to generate random password
"""





import random

def generate_password(length):

    #all character string
    ALL_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*/?-+=,.|~"

    password = ""

    #generate password
    for i in range(length):
        password += random.choice(ALL_CHARS)

    return password