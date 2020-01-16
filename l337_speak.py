to_replace = ["a", "e", "g", "i", "o", "s", "t"]

user_input = input("\nEnter a string or copy paste something in. Your speech will be the L337357... \n\n")
leet_string = ''
for x in user_input:
    if x.lower() in to_replace:
        if x.lower() == "a":
            leet_string += "4"
        elif x.lower() == "e":
            leet_string += "3"
        elif x.lower() == "g":
            leet_string += "6"
        elif x.lower() == "i":
            leet_string += "1"
        elif x.lower() == "o":
            leet_string += "0"
        elif x.lower() == "s":
            leet_string += "5"
        elif x.lower() == "t":
            leet_string += "7"
    else:
        leet_string += x
print("\n\n\n")
print (leet_string + "\n-S0m3 l337 H4x0r")
print("\n\n\n")