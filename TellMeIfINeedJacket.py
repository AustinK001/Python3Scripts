import os

def foo(temp, user_input):
  if temp > 7:
      return user_input + "It is warm"
  else:
        return user_input +  "It is cold"

user_input = input("Enter your name")
print(user_input)
x = int(input("Enter an integer >>>"))
print(foo(x, user_input))
