input_1 = input("Enter any word. \n")
#seems so incredibly verbose but this is my first attmpt.
count = 0
while len(input_1) > count:
    if (input_1[count].lower() == "a" and input_1[count + 1].lower())  == "a":
        print(input_1[: count] + (input_1[count] * 5) + input_1[(count + 2):] )
        break
    elif (input_1[count].lower() == "e" and input_1[count + 1].lower())  == "e":
        print(input_1[: count] + (input_1[count] * 5) + input_1[(count + 2):] )
        break
    elif (input_1[count].lower() == "i" and input_1[count + 1].lower())  == "i":
        print(input_1[: count] + (input_1[count] * 5) + input_1[(count + 2):] )
        break
    elif (input_1[count].lower() == "o" and input_1[count + 1].lower())  == "o":
        print(input_1[: count] + (input_1[count] * 5) + input_1[(count + 2):] )
        break
    elif (input_1[count].lower() == "u" and input_1[count + 1].lower())  == "u":
        print(input_1[: count] + (input_1[count] * 5) + input_1[(count + 2):] )
        break
    count += 1
    
if count == len(input_1):
    print(input_1)