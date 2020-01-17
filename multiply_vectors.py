#takes 2 lists and multiplies each corresponding index by each other.
list_1 = [2, 4, 6, 8]
list_2 = [12, 3, 5, 6]

def multiply_vector(x, y):
    product = []
    i = 0
    while i < len(x):
        product.append(x[i] * y[i])
        i += 1
    return product
    
print(multiply_vector(list_1, list_2))