import random

r = 5000
file = open("lists.txt", 'w')
for index in range(10):
    for ins in range(r):
        file.write(str(random.randint(1, 100000)) + ' ')
    file.write('\n')
    r += 5000
file.close()