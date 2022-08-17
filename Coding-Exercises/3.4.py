f = open('3.4.txt', 'w')
f.write("I like learning Python because it is easy.")
f.write("\nI want to build web apps using Python.\nI will use Python frameworks.\nI want to earn a lot of money.")

f = open('3.4.txt')
print(f.read())

f.close()
