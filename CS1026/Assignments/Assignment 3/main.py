"""
************************************************
CS 1026 - Assignment 3 – YouTube Emotions
Code by: Yiwei Dong
Student ID: ydong445
File created: Nov 18, 2024
************************************************
This file is used to ask user input and calculate YouTube comment emotion value
"""

import os.path
from emotions import *

VALID_COUNTRIES = ['bangladesh', 'brazil', 'canada', 'china', 'egypt',
                   'france', 'germany', 'india', 'iran', 'japan', 'mexico',
                   'nigeria', 'pakistan', 'russia', 'south korea', 'turkey',
                   'united kingdom',  'united states']


def ask_user_for_input():

    #get keyword file name
    try:
        keyword_file = input("Input keyword file (ending in .tsv): ")
    except EOFError:
        raise ValueError("Keyword file does not end in .tsv!")

    if not keyword_file.endswith(".tsv"):
        raise ValueError("Keyword file does not end in .tsv!")
    elif not os.path.exists(keyword_file):
        raise IOError(f"{keyword_file} does not exist!")

    #get comment file name
    try:
        comment_file = input("Input comment file (ending in .csv): ")
    except EOFError:
        raise ValueError("Comments file does not end in .csv!")

    if not comment_file.endswith(".csv"):
        print("Error: Comment file does not end in .csv!")
    elif not os.path.exists(comment_file):
        print(f"Error: {comment_file} does not exist!")

    #get country
    try:
        country = input('Input a country to analyze (or "all" for all countries): ').lower()
    except EOFError:
        raise ValueError(f"{country} is not a valid country to filter by!")

    if country != "all" and country not in VALID_COUNTRIES:
        print(f"Error: {country} is not a valid country to filter by!")

    #get report file name
    try:
        report_file = input("Input the name of the report file (ending in .txt): ")
    except EOFError:
        raise ValueError("Report file does not end in .txt!")

    if not report_file.endswith(".txt"):
        raise ValueError("Report file does not end in .txt!")
    elif os.path.exists(report_file):
        raise IOError(f"{report_file} already exists!")


    #return valid file
    return keyword_file, comment_file, country, report_file

def main():

    keyword_file, comment_file, country, report_file = ask_user_for_input() #get all user input

    keywords = make_keyword_dict(keyword_file)

    comment_list = make_comments_list(country, comment_file)

    most_common_emotion = make_report(comment_list, keywords, report_file)

    print(f"Most common emotion is: {most_common_emotion}")


if __name__ == "__main__":
    main()
