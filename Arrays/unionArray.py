# Given two arrays a[] and b[] of size n and m respectively. The task is to find union between these two arrays.
#
# Union of the two arrays can be defined as the set containing
# distinct elements from both the arrays. If there are repetitions, then only one occurrence of element should be printed in the union.
#
# Input:
# 5 3
# 1 2 3 4 5
# 1 2 3
# Output:
# 5
# Explanation:
# 1, 2, 3, 4 and 5 are the
# elements which comes in the union set
# of both arrays. So count is 5.

def unionarr(arr1,arr2):
    m = len(arr1)
    n = len(arr2)
    res = []
    if m > n:
        for i in arr2:
            if i not in arr1:
                res.append(i)
        res.extend(arr1)
    else:
        for i in arr1:
            if i not in arr2:
                res.append(i)
        res.extend(arr1)

    print("Total number of elements after union 2 arrays in ",res," is ",len(res))

if __name__ == "__main__":
    arr1 = [1,2,3,4,5]
    arr2 = [1,2,3,6]
    unionarr(arr1,arr2)