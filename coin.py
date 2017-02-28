#! python3

import random

count = 0
heads = 0
tails = 0
print('Making a coin roll simulation')
while count < 100:
    if random.randint(0, 1) == 0:
        heads += 1
    else:
        tails += 1
    count += 1

print('Heads: ', heads, '\nTails: ', tails)