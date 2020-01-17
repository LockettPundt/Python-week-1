#asks the user for a number and prints out a n*n square of "*"

n = int(input("Enter the number that you would like your square to be.\n"))
i = n
while i > 0:
    print("*" * n)
    i -= 1