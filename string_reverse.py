#quick way to reverse a string.
user_input = input("Enter a word or string... \n")
print (user_input[::-1])
reversed = ''
#longer way using a for loop.
count = len(user_input) - 1
while count >= 0:
    reversed += user_input[count]
    count -= 1
print(reversed)
