#while loop example

title = "Here is a string of some length."

STOP = 10
count = 0
while count < STOP:
    print(count)
    count += 1

#while loop that iterates through title
count_2 = 0
while count_2 < len(title):
    print(title[count_2])
    count_2 += 1

#print backwards
count_3 = len(title) - 1
while count_3 >= 0:
    print(title[count_3])
    count_3 -= 1