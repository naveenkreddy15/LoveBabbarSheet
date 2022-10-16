# Given an array, rotate the array by one position in clock-wise direction.
#
# Input:
# N = 5
# A[] = {1, 2, 3, 4, 5}
# Output:
# 5 1 2 3 4

def rotateArray(arr):
    i = 0
    j = len(arr) - 1
    while i != j:
        arr[i], arr[j] = arr[j], arr[i]
        i = i + 1
    pass

    print(arr)

if __name__ =="__main__":
    rotateArray([2,3,4,5])



