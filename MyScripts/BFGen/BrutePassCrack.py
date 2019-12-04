import random
import sys
from io import StringIO
from random import choice
path = 'Outputfile.txt'
list = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
trys = 10000000
length = 5
for i in range (0 , trys) :
    #Remember to add random.choice() to A in order to set the rows
    #New instances must be based on the length of the password searched for
    A = random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list)
    B = "".join(A)
    f = open("Outputfile.txt", "a")

    print("Try:",i , B, file=f)

    f.close()
    i += 1
