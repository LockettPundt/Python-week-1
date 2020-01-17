#user is asked for 4 numbers and they are put into a list. the sum of that list is printed.
sum_list = []
sum_list.append(int(input("Enter a number.")))
sum_list.append(int(input("Enter a number.")))
sum_list.append(int(input("Enter a number.")))
sum_list.append(int(input("Enter a number.")))
sum = 0
for x in sum_list:
    sum += x

print(sum)
