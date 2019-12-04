#!/usr/bin/env python3

#Open the file
if os.cwd() == '/Users/admin/Desktop/UniversalTestFiles' :
os.chdir("Desktop/UniversalTestFiles")
else :
fobj = open("Test2.txt")
text = fobj.read().strip().split()

#Conditions
while True:
    s = input("Enter a string: ") #Takes input of a string from user
    if s == "": #if no value is entered for the string
        continue
    if s in text: #string in present in the text file
        print("Matched")
        break
    else: #string is absent in the text file
        print("No such string found,try again")
        continue
