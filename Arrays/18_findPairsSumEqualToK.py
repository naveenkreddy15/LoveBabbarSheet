# # Given an array of N integers, and an integer K,
# # find the number of pairs of elements in the array whose sum is equal to K.
#
# Input:
# N = 4, K = 6
# arr[] = {1, 5, 7, 1}
# Output: 2
# Explanation:
# arr[0] + arr[1] = 1 + 5 = 6
# and arr[1] + arr[3] = 5 + 1 = 6.

def findPairs(arr,k):
    n = len(arr)
    res = []
    for i in arr:
        elem = k - i
        if elem in arr and i >= elem:
            res.append([i,elem])
    return res

if __name__ == "__main__":
    arr = [1,5,7,-1]
    k = 6
    print(findPairs(arr,k))