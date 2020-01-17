#prompt the user for dimension and create an empty box made of "*".
height = int(input("Enter the height of your box. \n"))
width = int(input("Enter the width of your box. \n"))
i = height
j = width
middle = ''
while j > 0:
    if j == width:
        middle += "*"
    elif j == 1:
        middle += "*"
    else:
        middle += " "
    j -= 1
while i > 0:
    if i == height:
        print("*" * width)
    elif i == 1:
        print("*" * width)
    else:
        print(middle)
    i -= 1
