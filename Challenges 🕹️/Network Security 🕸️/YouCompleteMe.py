#!/usr/bin/env python3
import string

with open('./words.txt', 'rb') as f:
    words = list(sorted([word.strip() for word in f.readlines()]))

ascii_all = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + '_'
risp_len = [3952, 825, 23, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1] # len delle risposte della binsearch

def next_char(char):
    return (ord(char) + 1).to_bytes(1, 'big')

def get_words_by_prefix(prefix):
    prefix, last_char = prefix[:-1], prefix[-1].to_bytes(1, 'big')
    lower_bound = prefix + last_char
    upper_bound = prefix + next_char(last_char)

    return [w for w in words if lower_bound <= w < upper_bound]

def trova(pre, pos):
    if pos == len(risp_len):
        print(pre)
        return
    
    for i in ascii_all:
        if len(get_words_by_prefix(pre + i.encode())) == risp_len[pos]:
            trova(pre + i.encode(), pos + 1)

trova(b'', 0)