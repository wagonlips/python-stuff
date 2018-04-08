#!/usr/bin/env python

def jj(l="null"):
    if type(l) == int:
        for value,key in sorted(set(myblob.tags)):
            if key[0] == "J" and len(value) == l:
                print key,value
    else:
        for value,key in sorted(set(myblob.tags)):
            if key[0] == "J":
                print key,value

