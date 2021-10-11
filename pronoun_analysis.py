#!/usr/bin/python
import json
import re
import os
import glob
from celery import Celery


app = Celery('tasks', backend='rpc://', broker='pyamqp://ubuntu@192.168.2.81//')

@app.task
def tweet_analysis():
    data = []
    path = '/home/ubuntu/lab_3/data'
    for filename in glob.glob(os.path.join(path, '*')):
        with open(os.path.join(os.getcwd(), filename), 'r') as f: # open in readonly mode
            for line in f: #for each line in our file
                if line.strip() and 'retweeted_status' not in json.loads(line):
                    dat = json.loads(line)
                    data.append(dat["text"])
    #print("Tweet text loaded, next map")
    keylist = ['han', 'hon', 'den', 'det', 'denna', 'denne', 'hen']
    map_word = []
    for el in data:
        words = re.split('[:",. ]',el)
        #print(type(words))
        for word in words: #search all the words of each text
            word = word.lower()
            word = word.strip()
            if word in keylist: #if the word is in the keylist
                map_word.append(word)
    word_set = {"han", "hon", "den", "det", "denna", "denne", "hen"}
    word_dict = dict.fromkeys(word_set,0)
    for word in map_word:
        key, value = word , 1
        if key not in word_dict:
            word_dict[key] = value
        else:
            word_dict[key] += value

    #Get sorted list of keys
    keys = [(k, word_dict[k]) for k in sorted(word_dict, key=word_dict.get, reverse=True)]

    return keys
