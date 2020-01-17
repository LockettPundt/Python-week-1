#takes a user number and prints a beautiful triangle for them.
num = int(input("Enter a number and watch a beautiful triangle appear.\n"))
i = 1
x = num
while i < num:
    if i == 1:
        print((" " * num) + "*")
    else:
        print((" " * num) + ("*" * i))
    i += 2
    num -= 1
    
