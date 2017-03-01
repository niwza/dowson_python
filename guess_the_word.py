#! python3

import random

WORDLIST = ['advice',
            'anger',
            'answer',
            'apple',
            'arithmetic',
            'badge',
            'basket',
            'basketball',
            'battle',
            'beast',
            'beetle',
            'beggar',
            'brain',
            'branch',
            'bubble',
            'bucket',
            'cactus',
            'cannon',
            'cattle',
            'celery',
            'cellar',
            'cloth',
            'coach',
            'coast',
            'crate',
            'cream',
            'daughter',
            'donkey',
            'drug',
            'earthquake',
            'feast',
            'fifth',
            'finger',
            'flock',
            'frame',
            'furniture',
            'geese',
            'ghost',
            'giraffe',
            'governor',
            'honey',
            'hope',
            'hydrant',
            'icicle',
            'income',
            'island',
            'jeans',
            'judge',
            'lace',
            'lamp',
            'lettuce',
            'marble',
            'month',
            'north',
            'ocean',
            'patch',
            'plane',
            'playground',
            'poison',
            'riddle',
            'rifle',
            'scale',
            'seashore',
            'sheet',
            'sidewalk',
            'skate',
            'slave',
            'sleet',
            'smoke',
            'stage',
            'station',
            'thrill',
            'throat',
            'throne',
            'title',
            'toothbrush',
            'turkey',
            'underwear',
            'vacation',
            'vegetable',
            'visitor',
            'voyage',
            'year']

word = random.choice(WORDLIST)
revealed = []
tries = 5

def show_word(word, revealed):
    result = ''
    for i in range(len(word)):
        if i in revealed:
            result += word[i]
        else:
            result += '*'
    return result

print('I\'m thinking of a word', show_word(word, revealed))
print('You can guess 5 letters.')

while tries:
    letter = input('Make your guess. Enter a letter: ')
    if letter.lower() in word:
        print('Yes. There is such letter in the word')
        for i in range(len(word)):
            if letter == word[i]:
                revealed += [i]
    else:
        print('No. There is no such letter in the word')
    print(show_word(word, revealed))
    tries -= 1

guess = input('Now you have to guess the hole word.\n').lower()
if guess == word:
    print('You won!')
else:
    print('You loose!')

print('My word was', word)
