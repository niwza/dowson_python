#! python3

# In this game. You should think of a number between 1 and 100.
# Computer will try to guess it.

lower = 1
higher = 100
tries = 1

while True:
    guess = ( lower + higher ) // 2
    print('You\'re thinking of', guess)
    answer = int(input('Press:\n1. If your number is lower\n2. If your number is higher\n3. If I\'ve guessed.\n'))
    if answer == 1:
        higher = guess
    elif answer == 2:
        lower = guess
    elif answer == 3:
        break
    else:
        print('Wrong input. Try again.')
        continue
    tries += 1

print('You thought of', guess, 'It took me', tries, 'to guess your number.')