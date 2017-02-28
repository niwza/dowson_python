#! python3

# Guess the number game.
import random

print('''
    Hello. Computer thinks of a random number between 1 and 100.
    You should try to guess that number.
      ''')

number = random.randint(1, 100)
guess = int(input('Enter your guess: '))
count = 1
while guess != number:
    if guess > number:
        print('I\'m thinking of a lower number.')
    else:
        print('I\'m thinking of a higher number.')
    guess = int(input('Enter your next guess: '))
    count += 1
print('You won!')
print('It took you ', count, 'guesses.')