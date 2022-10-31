# # Given an array Arr[] that contains N integers (may be positive, negative or zero).
# # Find the product of the maximum product subarray.
# Input:
# N = 5
# Arr[] = {6, -3, -10, 0, 2}
# Output: 180
# Explanation: Subarray with maximum product
# is [6, -3, -10] which gives product as 180.

def maxProductSubArray(arr):
    maxProd = arr[0]
    left = 0
    n = len(arr)

    while(left < n):
        right = left + 1
        currProd = arr[left]
        while(right < n):
            currProd = currProd * arr[right]
            maxProd = max(maxProd,currProd)
            right = right + 1
        left = left + 1

    return maxProd

if __name__=="__main__":
    print(maxProductSubArray([6,0,-10,0,2]))
