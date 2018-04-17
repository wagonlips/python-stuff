#!/usr/bin/env python
import sys
import twitter
import textblob
from textblob import TextBlob
def o(blob):
    global myblob
    with open(r"/home/sean/Documents/text-blobs/" + blob + "") as infile:
        data = infile.read()
        myblob = TextBlob(data)

def p(part,l="null"):
    if type(l) == int:
        for value,key in sorted(set(myblob.tags)):
            if key[0] == part and len(value) == l:
                print key,value
    else:
        if len(part) == 1:
            for value,key in sorted(set(myblob.tags)):
                if key[0] == part:
                    print key,value
        else:
            for value,key in sorted(set(myblob.tags)):
                if key == part:
                    print key,value

def start(chars,l="null"):
    if type(l) == int:
        for value,key in sorted(myblob.tags):
            if value.lower().startswith(chars) and len(value) == l:
                print key,value
    else:
        for value,key in sorted(myblob.tags):
            if value.lower().startswith(chars):
                print key,value


def end(chars,l="null"):
    if type(l) == int:
        for value,key in sorted(myblob.tags):
            if value.lower().endswith(chars) and len(value) == l:
                print key,value
    else:
        for value,key in sorted(myblob.tags):
            if value.lower().endswith(chars):
                print key,value
