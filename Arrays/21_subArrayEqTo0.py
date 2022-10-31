# Given an array of positive and negative numbers.
# Find if there is a subarray (of size at-least one) with 0 sum.
#
# Input:
# 5
# 4 2 -3 1 6
#
# Output:
# Yes
#
# Explanation:
# 2, -3, 1 is the
# subarray
# with sum 0.

def subArray(arr):
    left = 0
    n = len(arr)

    res = []

    while (left < n):
        total = arr[left]
        right = left + 1

        while(right < n):
            total = total + arr[right]
            if total == 0:
                res.append(arr[left:right+1])
            right = right + 1
        left = left + 1

    return res

if __name__=="__main__":
    print(subArray([-4,-2,3,1,3]))