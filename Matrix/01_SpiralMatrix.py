# Given a 2D array, print it in spiral form.
#
# Input:  {{1,    2,   3,   4},
#               {5,    6,   7,   8},
#              {9,   10,  11,  12},
#             {13,  14,  15,  16 }}
# Output: 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
# Explanation: The output is matrix in spiral format.

def spiralFormat(arr,row_end,col_end):
    row_start = 0
    col_start = 0
    res = []
    while (row_start < row_end and col_start < col_end):
        for i in range(col_start,col_end):
            res.append(arr[row_start][i])
        row_start = row_start + 1

        for i in range(row_start,row_end):
            res.append(arr[i][col_end-1])
        col_end = col_end - 1

        if (row_start < row_end):
            for i in range(col_end-1,col_start-1,-1):
                res.append(arr[row_end-1][i])
            row_end = row_end - 1

        if (col_start < col_end):
            for i in range(row_end-1,row_start-1,-1):
                res.append(arr[i][col_start])
            col_start = col_start + 1

    for i in range(len(res)):
        print(res[i],end=' ')

if __name__ == "__main__":
    arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    col_end = len(arr)
    row_end= len(arr[0])

    spiralFormat(arr,row_end,col_end)
