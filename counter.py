#! python3

start = int(input('Input starting number'))
stop = int(input('Input last number'))
interval = int(input('Input interval'))

for i in range(start, stop, interval):
    print(i, end=' ')