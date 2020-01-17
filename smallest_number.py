#takes a list and return the smallest number within the list.
some_list = [40, 13, 1000, 23, 10001, 10000000, 497860, 867, 23, 7, 2355]
def whats_smaller(x):
    temp = x[0]
    for x in some_list:
        if x < temp:
            temp = x
    return temp


print(whats_smaller(some_list))
