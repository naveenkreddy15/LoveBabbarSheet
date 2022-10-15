# Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.
#
# Input:
# N = 5
# arr[]= {0 2 1 2 0}
# Output:
# 0 0 1 2 2
# Explanation:
# 0s 1s and 2s are segregated
# into ascending order.

def sortArray(arr):
    zeroCount = arr.count(0)
    oneCount = arr.count(1)
    twoCount = arr.count(2)
    res = [0]*zeroCount + [1]*oneCount + [2]*twoCount
    print("resultant of arr ",res)

if __name__ =="__main__":
    sortArray([0,2,2,0])
