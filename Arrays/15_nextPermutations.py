# Given an array arr[] of size N, the task is to print the lexicographically next greater permutation of the given array.
# If there does not exist any greater permutation, then print the lexicographically smallest permutation of the given array.
#
# Input: N = 6, arr = {1, 2, 3, 6, 5, 4}
# Output: {1, 2, 4, 3, 5, 6}
# Explanation: The next permutation of the given array is {1, 2, 4, 3, 5, 6}.
# https://www.nayuki.io/page/next-lexicographical-permutation-algorithm

def nxtPermutations(arr):
    i = j = len(arr)-1

    while i > 0 and arr[i-1] >= arr[i]:
        i = i - 1

    if i == 0:
       return arr.reverse()

    while arr[j] <= arr[i-1]:
        j = j -1

    arr[i-1],arr[j] = arr[j],arr[i-1]

    j = len(arr)-1

    while i < j:
        arr[i],arr[j]=arr[j],arr[i]
        i = i + 1
        j = j -1

    print("next permutation array is ",arr)

if __name__=="__main__":
    nxtPermutations([0, 1, 2, 5, 3, 3, 0])



