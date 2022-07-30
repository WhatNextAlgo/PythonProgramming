def findMinCost(twoDArray,row,col):
    if row == -1 or  col == -1:
        return float('inf')
    elif row == 0 and col == 0:
        return twoDArray[row][col]
    else:
        opt1 = findMinCost(twoDArray,row-1,col)
        opt2 = findMinCost(twoDArray,row,col-1)
        return twoDArray[row][col] + min(opt1,opt2)


TwoDList = [
    [4,7,8,6,4],
    [6,7,3,9,2],
    [3,8,1,2,4],
    [7,1,7,3,7],
    [2,9,8,9,3]]

print(findMinCost(TwoDList,4,4))