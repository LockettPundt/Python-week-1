#multiplies every index of a random list by a multiplier submitted by the user. 
num = int(input("Enter what you want to multiply the list by."))
import random
some_list = []

some_list.append(random.randint(1, 100))
some_list.append(random.randint(1, 100))
some_list.append(random.randint(1, 100))
some_list.append(random.randint(1, 100))
some_list.append(random.randint(1, 100))
some_list.append(random.randint(1, 100))
some_list.append(random.randint(1, 100))
some_list.append(random.randint(1, 100))

def list_multiplier(x, n):
    new_list = []
    for i in x:
        new_list.append(i * n)
    return new_list

print(list_multiplier(some_list, num))