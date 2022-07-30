def num_of_paths(matrix,row,col,cost):
    if cost < 0:
        return 0

    elif row == 0 and col == 0:
        if matrix[0][0] - cost == 0:
            return 1
        else:
            return 0

    elif row == 0:
        return num_of_paths(matrix,0,col-1,cost-matrix[row][col])
    elif col == 0:
        return num_of_paths(matrix,row-1,0,cost-matrix[row][col])
    else:
        opt1 =num_of_paths(matrix,row-1,col,cost-matrix[row][col])
        opt2 =num_of_paths(matrix,row,col-1,cost-matrix[row][col])
        return opt1 + opt2


matrix = [
    [4,7,1,6],
    [5,7,3,9],
    [3,2,1,2],
    [7,1,6,3]

]
print(num_of_paths(matrix,3,3,25))
    