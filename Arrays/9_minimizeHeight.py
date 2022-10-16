# Given an array arr[] denoting heights of N towers and a positive integer K.
#
# For each tower, you must perform exactly one of the following operations exactly once.
#
# Increase the height of the tower by K
# Decrease the height of the tower by K
# Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.
#
# Input:
# K = 2, N = 4
# Arr[] = {1, 5, 8, 10}
# Output:
# 5
# Explanation:
# The array can be modified as
# {3, 3, 6, 8}. The difference between
# the largest and the smallest is 8-3 = 5.

def tower(arr,k):
    arr.sort()
    minEle = min(arr)
    maxEle = max(arr)

    for i in range(len(arr)):
        if arr[i] == minEle:
            arr[i] = arr[i] + k
        elif arr[i] == maxEle:
            arr[i] = arr[i] - k
        elif arr[i] + k >= minEle and arr[i] + k <= maxEle-k:
            arr[i] = arr[i] + k
        else:
            arr[i] = arr[i]-k

    print("resultant array after adding/subtracting k from each element is ", arr)
    print("min difference between the between is ",max(arr) - min(arr))

if __name__=="__main__":
    tower([1,15,10],3)








