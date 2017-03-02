#! python3

# This program prints out all the words from a provided list in random order.

import random

wordlist = ['hell',
            'you',
            'ass',
            'kiss',
            'try',
            'example']

while wordlist:
    word = random.choice(wordlist)
    wordlist.remove(word)
    print(word)