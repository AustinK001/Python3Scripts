import random
import sys
from random import choice
path = 'Outputfile.txt'
list = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
trys = 10000000
length = 3
new = open(path, 'w')
print(new)
for i in range (0 , trys)   :
    #Remember to add random.choice() to A in order to set the correct amount of random
    #variable searches based on your grep search
    #New instances must be based on the length of the password searched for
    A = random.choice(list), random.choice(list), random.choice(list)
    B = "".join(A)
    f = open("Outputfile.txt", "a")
    print("Try:",i , B, "Out of:", trys, file=f)
    print("Try:",i ,"Out of:", trys , B)
    f.close()
    i += 1
