import numpy as np

def createMatrix(row,col):
    matrix = []
    for x in range(0,row):
        row = []
        for y in range(0,col):
            item = int(raw_input("Enter item [%s][%s]" %(x,y)))
            row.append(item)
        matrix.append(row)
    return matrix

def spiralMatrix(matrix, row, col):
    T = 0
    B = row - 1
    L = 0
    R = col - 1
    # 0 -> right 1 -> down 2->left 3->up
    dir = 0

    while(T<=B and L<=R):
        # import pdb;pdb.set_trace()
        if(dir == 0):
            for x in range(L,R+1):
                print matrix[T][x]
            T += 1
            dir = 1
        if(dir == 1):
            for x in range(T,B+1):
                print matrix[x][R]
            R -= 1
            dir = 2

        if(dir == 2):
            for x in range(R,L-1,-1):
                print matrix[B][x]
            B -= 1
            dir = 3

        if(dir == 3):
            for x in range(B,T-1,-1):
                print matrix[x][L]
            L += 1
            dir = 0

# row = int(raw_input("How many rows do you want in the matrix? "))
# col = int(raw_input("How many columns do you want in the matrix? "))
# matrix = createMatrix(row,col)
row = 4
col = 4
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
spiralMatrix(matrix, row, col)
# print(np.matrix(matrix))
