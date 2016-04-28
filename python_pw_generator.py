#!/usr/bin/python

# generate random password using *nix word list, numpy random
# meant to be an easy way to generate secure and somewhat memorable passwords

from numpy import random as r

# initialize lists
randchar = ['!','@','#','$','%','^','&','*']
words = []

# read words file (on Mac) into variable, strip extra chars and newlines
with open("/usr/share/dict/words") as f:
    for w in f.readlines():
        words.append(w.strip())

# randomly choose three-word pw, with no repeats (pretty unlikely anyway); replace first 'i' and/or 'e' with numbers
word_choices = r.choice(words, 3, replace=False)
word_choices = [w.replace('i','1', 1) if 'i' in w else w.replace('e','3', 1) for w in word_choices]

# insert random characters as delimiters, capitalize second word (just because)
# try this until you can kind of remember it!
print "Your new password is: " + word_choices[0] + r.choice(randchar) + word_choices[1].title() + r.choice(randchar) + word_choices[2]
del randchar, words, word_choices
