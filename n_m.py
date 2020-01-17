#user input one num to start, and it prints until it reaches the other number.
num_1 = int(input("Hi there. Enter any number to start on. \n"))
num_2 = int(input("What number would you like to end on? \n"))

def x_to_y(x, y):
    i = x
    while i <= y:
        print(i)
        i += 1

def y_to_x(x, y):
    i = x
    while i >= y:
        print(i)
        i -= 1

if (num_1 > num_2):
    y_to_x(num_1, num_2)
else:
    x_to_y(num_1, num_2)