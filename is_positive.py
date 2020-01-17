#returns all of the positive numbers in a list into another list.
#if you wanted to print them out seperately, you could for loop to iterate over the positives list.
import random
some_list = []

some_list.append(random.randint(-1000, 10000))
some_list.append(random.randint(-1000, 10000))
some_list.append(random.randint(-1000, 10000))
some_list.append(random.randint(-1000, 10000))
some_list.append(random.randint(-1000, 10000))
some_list.append(random.randint(-1000, 10000))
some_list.append(random.randint(-1000, 10000))
some_list.append(random.randint(-1000, 10000))
def is_positive(x):
    positives = []
    for i in x:
        if (i > 0):
            positives.append(i)
    return positives


print(is_positive(some_list))
