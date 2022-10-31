# Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
# Note: can you take care of the duplicates without using any additional Data Structure?
#
# Input:
# n1 = 6; A = {1, 5, 10, 20, 40, 80}
# n2 = 5; B = {6, 7, 20, 80, 100}
# n3 = 8; C = {3, 4, 15, 20, 30, 70, 80, 120}
# Output: 20 80
#
# Explanation: 20 and 80 are the only
# common elements in A, B and C.

def commonElements(arr1,arr2,arr3):
    minIter = min(len(arr1),len(arr2),len(arr3))
    res = set()

    for i in range(minIter):
        if minIter == len(arr1) and arr1[i] in arr2 and arr1[i] in arr3:
            res.add(arr1[i])
        elif minIter == len(arr2) and arr2[i] in arr1 and arr2[i] in arr3:
            res.add(arr2[i])
        elif minIter == len(arr3) and arr3[i] in arr2 and arr3[i] in arr1:
            res.add(arr3[i])

    return res

if __name__ == "__main__":
    arr1 = [1, 5, 10, 20, 40, 80]
    arr2 = [6, 7, 20, 80, 100]
    arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

    print(commonElements(arr1,arr2,arr3))

