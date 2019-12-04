import random
from random import choice

list = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
trys = 1000000
password = "pass"
for i in range (0 , trys) :
    #Remember to add random.choice() to A in order to set the rows
    #New instances must be based on the length of the password searched for
    A = random.choice(list), random.choice(list) , random.choice(list), random.choice(list)
    print("".join(A))
    i += 1
