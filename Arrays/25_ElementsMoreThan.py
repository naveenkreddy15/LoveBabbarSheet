# Given an array of size n and an integer k,
# find all elements in the array that appear more than n/k times.
#
# Input: arr[] = {3, 1, 2, 2, 1, 2, 3, 3}, k = 4
# Output: {2, 3}
# Explanation: Here n/k is 8/4 = 2, therefore 2 appears 3 times in the array that is greater than 2 and 3 appears 3 times in the array that is greater than 2
#
# Input: arr[] = {9, 8, 7, 9, 2, 9, 7}, k = 3
# Output: {9}
# Explanation: Here n/k is 7/3 = 2, therefore 9 appears 3 times in the array that is greater than 2

from collections import Counter

def findElements(arr,k):
    arr_dict = Counter(arr)
    res = []
    target = int(len(arr)/k)
    for key,val in arr_dict.items():
        if val > target:
            res.append(key)

    return res

if __name__=="__main__":
    print(findElements([9, 8, 7, 9, 2, 9, 7],3))
