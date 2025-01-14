f = open("text.txt", "r")
positive = []
neutral = []
negative = []

for line in f:
    entries = line.split(",")
    entries[1] = int(entries[1].rstrip("\n"))

    if entries[1] == 20:
        positive.append(entries[0])
    elif entries[1] == 0:
        neutral.append(entries[0])
    else:
        negative.append(entries[0])

tweet = "I really am very happy for you I love the weather I am also sad and have some regrets about being so tired"
tweet_words = tweet.split()
sentiment = 0
for word in tweet_words:
    if word in positive:
        sentiment += 20
    elif word in negative:
        sentiment -= 10

print("The positive keywords are {}".format(positive))
print("The neutral keywords are {}".format(neutral))
print("The negative keywords are {}".format(negative))
print("The sentiment of the tweet is {}".format(sentiment))

f.close()


text = open("text.txt", "r")
myfile = open("myfile.txt", "w") #use "w" to write
line = text.read() #miss ()
words = line.split()
for word in words:
    print(word) #don't need + "\n"
    myfile.write(word + "\n") # need \n here

    
text.close()
myfile.close()