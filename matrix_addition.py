#takes matrixes of any length and adds them together.
matrix_1 = [[1, 2], [11, 6]]
matrix_2 = [[4, 6], [25,5]]

def matrix_adder(x, y):
    if (len(x) == len(y)):
        sum_matrix = []
        i = 0
        j = 0
        while i < len(x):
            temp = []
            while j < len(x[i]):
                temp.append(x[i][j] + y[i][j])
                j += 1
            i += 1
            j = 0
            sum_matrix.append(temp)
    return sum_matrix
    
print(matrix_adder(matrix_1, matrix_2))
