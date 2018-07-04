#!/usr/bin/env python
doc_list=['The Learn Python Challenge Casino', 'They bought a car, and a horse', 'Casinoville?']
alt_list=['aaa','bbb','ccc']
def word_search(doc_list, keyword):
    words = doc_list.split()
    print(words.index(keyword))

word_search(alt_list, "bbb")
