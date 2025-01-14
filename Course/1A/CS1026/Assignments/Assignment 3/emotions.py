"""
************************************************
CS 1026 - Assignment 3 – YouTube Emotions
Code by: Yiwei Dong
Student ID: ydong445
File created: Nov 18, 2024
************************************************
This file is used to make function to clean_text, make keyword dict,
classify_comment_emotion,make_comments_list and make the final report file
"""

from itertools import count
from typing import final

EMOTIONS = ['anger', 'joy', 'fear', 'trust', 'sadness', 'anticipation']


def clean_text(comment):
    clear_text = ""

    for letter in comment:

        if letter.lower() not in "abcdefghijklmnopqrstuvwxyz ": #check if letters are not letters
            letter = " " #change it to space
            clear_text += letter #add to result string

        else:
            clear_text += letter #add to result sting

    return clear_text.lower()


def make_keyword_dict(keyword_file_name):
    file = open(keyword_file_name, "r") #open file

    try:
        keyword_dict = {}

        for line in file:
            line = line.strip()
            line = line.split() #split to
            #print(line)        #used to debug

            emotion_values_dict = {"anger": 0, "joy": 0, "fear": 0, "trust": 0, "sadness": 0, "anticipation": 0}

            word = line[0]
            #print(word)
            emotion_values_dict["anger"] = int(line[1])
            emotion_values_dict["joy"] = int(line[2])
            emotion_values_dict["fear"] = int(line[3])
            emotion_values_dict["trust"] = int(line[4])
            emotion_values_dict["sadness"] = int(line[5])
            emotion_values_dict["anticipation"] = int(line[6])

            keyword_dict[word] = emotion_values_dict #make result dictionary{word: values dict}


    finally:
         file.close()# Ensure the file is closed after processing
    return keyword_dict


def classify_comment_emotion(comment, keywords):

    cleaned_comment = clean_text(comment) #get the cleaned comment

    emotion_total = {"anger": 0, "joy": 0, "fear": 0, "trust": 0, "sadness": 0, "anticipation": 0}

    words = cleaned_comment.split() #split comment to words

    for word in words:
        if word in keywords:
            for emotion, value in keywords[word].items():
                emotion_total[emotion] += value #calculate words emotion value


    emotion_king = ""
    n = -1
    priority_order = ['anger', 'joy', 'fear', 'trust', 'sadness', 'anticipation']

    for emotion in priority_order:
        value = emotion_total[emotion]
        if value > n:
            n = value
            emotion_king = emotion #find the emotion king


    return emotion_king



def make_comments_list(filter_country, comments_file_name):

    comments_list = []

    file = open(comments_file_name, "r") #open file

    try:

        for line in file:
            line = line.strip()
            line = line.split(",")

            comment_id = int(line[0].strip())
            username = line[1].strip()
            country = line[2].lower()
            text = line[3].strip() #read file and process the information

            if filter_country.lower() == "all" or filter_country.lower() == country:
                comments_list.append({"comment_id": comment_id,
                                      "username": username,
                                      "country": country,
                                      "text": text
                                      })


    finally:
        file.close()

    return comments_list





def make_report(comment_list, keywords, report_filename):

    emotion_totals = {'anger': 0, 'joy': 0, 'fear': 0, 'trust': 0, 'sadness': 0, 'anticipation': 0}
    report_file = None

    if not comment_list:
        raise RuntimeError("No comments in dataset!")

    try:

        for comment in comment_list:
            emotion = classify_comment_emotion(comment["text"], keywords)
            emotion_totals[emotion] += 1 #process comment and calculate emotion value

        total = sum(emotion_totals.values()) #calculate how many comments have

        emotion_king = ""
        n = -1
        priority_order = ['anger', 'joy', 'fear', 'trust', 'sadness', 'anticipation']

        for emotion in priority_order:
            value = emotion_totals[emotion]
            if value > n:
                n = value
                emotion_king = emotion #find emotiong king

        emotion_percent = {}
        for emotion in emotion_totals:
            emotion_percent[emotion] = round((emotion_totals[emotion] / total) * 100, 2) #calculate the percentage

        report_lines = [f"Most Common Emotion: {emotion_king}\n"]
        report_lines.append("\nEmotion Totals\n")
        for emotion in priority_order:
            report_lines.append(f"{emotion}: {emotion_totals[emotion]} ({emotion_percent[emotion]}%)\n")
        #make what should write to report file

        report_file = open(report_filename, "w")
        report_file.writelines(report_lines)

        return emotion_king


    except RuntimeError as e:
        raise e

    finally:
        if report_file:
            report_file.close()



#These are used to test function
#****************************************************
#print(clean_text("This4is-an example. It's a b*t silly."))

#print(make_keyword_dict("keywords.tsv"))

#keywords = make_keyword_dict("keywords.tsv")
#comment_list = make_comments("all", "comments.csv")

#make_report(comment_list, keywords, "text.txt")

#print(classify_comment_emotion("The excavation scenes in the movie were excellent but the unnecessary derision of the hero's motives seemed unfair. His eventuality of success was not adequately showcased.", keywords))

#print(make_comments("all", "comments.csv"))
#print(make_comments("brazil", "comments.csv"))
#print(make_comments("not a real country", "comments.csv"))
