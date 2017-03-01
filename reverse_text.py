#! python3

text = input('Enter a text to be reversed: ')
res = ''

for i in range(-1, -len(text) - 1, -1):
    res += text[i]

print(res)