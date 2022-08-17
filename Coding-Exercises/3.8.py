import os

f = open('3.4.txt')
print(f.read())

for x in f:
    print(x)

f.close()

if os.path.exists('3.4.txt'):
    os.remove('3.4.txt')
else:
    print('file does not exist')
