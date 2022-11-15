# Given a square matrix, turn it by 90 degrees in a clockwise direction without using any extra space.
#
# Input:
# 1 2 3
# 4 5 6
# 7 8 9
# Output:
# 7 4 1
# 8 5 2
# 9 6 3

def squareMatrix(arr):
    col_start = 0
    row_end = len(arr[0])
    res=[]

    for j in range(len(arr)):
        for i in range(row_end-1,-1,-1):
            res.append(arr[i][j])

    return res

if __name__ == "__main__":
    arr = [[1,2,3],[4,5,6],[7,8,9]]
    print(squareMatrix(arr))
