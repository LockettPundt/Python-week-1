#takes a list and return the largest number within the list.
some_list = [1, 13, 1000, 23, 10001, 10000000, 497860, 867, 23, 2355]
def whats_larger(x):
    temp = 0
    for x in some_list:
        if x > temp:
            temp = x
    return temp


print(whats_larger(some_list))
