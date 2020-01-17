#creates a banner of "*" around the string provided by the user.

user_input = input("Enter a String.\n")

input_length = len(user_input + "    ")
print("\n")
print("*" * input_length)
print("* " + user_input + " *")
print("*" * input_length)
print("\n")
