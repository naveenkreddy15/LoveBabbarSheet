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

def kadane(arr):
    currSum = 0
    maxSum = 0
    bstart = bend = 0
    start = 0

    for i in range(len(arr)):
        currSum = currSum + arr[i]

        if currSum > maxSum:
            maxSum = currSum
            bstart = start
            bend = i
        if currSum <= 0:
            start = i + 1
            currSum =  0

    print("Max sum of subarray is ",maxSum)
    print("Subarray forming maxsum is ",bstart,bend,arr[bstart:bend+1])

if __name__ =="__main__":
    kadane([-1,2,3,-4,-6,3,1,2,-2,9])
