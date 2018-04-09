#!/usr/bin/env python
import sys
import textblob
from textblob import TextBlob
def o(blob):
    global myblob
    with open(r"/home/sean/Documents/text-blobs/" + blob + "") as infile:
        data = infile.read()
        myblob = TextBlob(data)

def jj(l="null"):
    if type(l) == int:
        for value,key in sorted(set(myblob.tags)):
            if key[0] == "J" and len(value) == l:
                print key,value
    else:
        for value,key in sorted(set(myblob.tags)):
            if key[0] == "J":
                print key,value

def p(part,l="null"):
    if type(l) == int:
        for value,key in sorted(set(myblob.tags)):
            if key[0] == part and len(value) == l:
                print key,value
    else:
        for value,key in sorted(set(myblob.tags)):
            if key == part:
                print key,value

def start(chars):
    for value,key in sorted(myblob.tags):
        if value.lower().startswith(chars):
            print key,value


def end(chars):
    for value,key in sorted(myblob.tags):
        if value.lower().endswith(chars):
            print key,value
