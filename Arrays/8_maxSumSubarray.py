# Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.
#
# Input:
# N = 5
# Arr[] = {1,2,3,-2,5}
# Output:
# 9
# Explanation:
# Max subarray sum is 9
# of elements (1, 2, 3, -2, 5) which
# is a contiguous subarray.
import sys


def maxSubArray(arr):
    currSum = 0
    maxSum = sys.maxsize * -1
    start = 0
    end = 0
    s = 0

    for i in range(len(arr)):
        currSum = currSum + arr[i]

        if currSum > maxSum:
            maxSum = currSum
            start = s
            end = i

        if currSum < 0:
            currSum = 0
            s = s + 1

    print("Max sum Subarray is ",maxSum)
    print("Max Sum Subarray is ",arr[start:end+1])


if __name__ =="__main__":
    maxSubArray([-2, -3,-4, -1, -2, -1, -5, -3])








