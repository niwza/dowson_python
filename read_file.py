#! python3

myfile = open('myfile.txt')
text = myfile.read()
myfile.close()
print(text)