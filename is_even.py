#returns all of the even numbers in the list.
import random
some_list = []

some_list.append(random.randint(1, 100000))
some_list.append(random.randint(1, 100000))
some_list.append(random.randint(1, 100000))
some_list.append(random.randint(1, 100000))
some_list.append(random.randint(1, 100000))
some_list.append(random.randint(1, 100000))
some_list.append(random.randint(1, 100000))
some_list.append(random.randint(1, 100000))
def is_even(x):
    evens = []
    for i in x:
        if (i % 2 == 0):
            evens.append(i)
    return evens

print(is_even(some_list))
