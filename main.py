# This is a sample Python script.
#Lets Consider a sample file containing each tweet on single line just like a csv file which has one record in a line
import re
slur =["bad","harmful"]   #set of slur word
tweet_list =[] #here each tweet will be stored in list format
file=open("tweet","r")
for x in file:
    tweet_list.append(x)
for x in tweet_list:
    words=re.split(' |\n',x)
    profanity = 0  # initial profanity set to zero
    for y in words:
        if y in slur:
            profanity += 1
    if profanity:
        print('The degree of profanity of "'+x+'" tweet is '+str(profanity)) #we can set the output as per our requirements
