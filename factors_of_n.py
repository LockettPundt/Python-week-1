#takes a number from user input and prints our all the numbers that it is divisible by.
num = int(input("Enter a number and I'll return all of the numbers that are factors of the number.\n"))
i = 1
num_array = []

while i <= num:
    if (num % i == 0):
        num_array.append(i)
    i += 1
print(num_array)
    