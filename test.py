import os
def function(user_input) :

    string_lastname = str("Kehrer")
    B = user_input[0].upper()
    C = user_input[1:len(user_input)]
    A = "Hello how are you {0} {1}".format(B + C, string_lastname)
    return A
user_input = input("Enter your name:")
print(function(user_input))
