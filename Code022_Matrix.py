import numpy as np

def matrices(row,col):
    matrix = []
    for x in range(0,row):
        row = []
        for y in range(0,col):
            item = int(raw_input("Enter item [%s][%s]" %(x,y)))
            row.append(item)
        matrix.append(row)
    return matrix

row = int(raw_input("How many rows do you want in the matrix? "))
col = int(raw_input("How many columns do you want in the matrix? "))
matrix = matrices(row,col)
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(np.matrix(matrix))
