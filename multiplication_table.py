#takes a number from the user and prints out a multiplication table * 10. so "3".... 1x1 - 1x10... 3x1 - 3x10.
num = int(input("Enter a number and I'll print all the multiplication tables for that number."))
i = 1
j = 1

while i <= num:
    while j <= 10:
        print("%s x %s = %s" % (i, j, i * j))
        j += 1
    j = 1
    print("\n")
    i += 1
