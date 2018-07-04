#!/usr/bin/python3
import string
import itertools

def alphai(string,num):
    '''increment the characters of a string of lowercase letters'''
    for i in string:
        j = ord(i)+num
        if j < 123:
            print(chr(j),end="")
        elif j >= 123:
            j = j - 26
            print(chr(j),end="")
    print()



