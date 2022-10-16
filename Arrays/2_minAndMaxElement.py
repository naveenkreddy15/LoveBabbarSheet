# Given an array of size N. The task is to find the maximum and the minimum element of the array using the minimum number of comparisons.
#
# Input: arr[] = {3, 5, 4, 1, 9}
# Output: Minimum element is: 1
#               Maximum element is: 9
#
# Input: arr[] = {22, 14, 8, 17, 35, 3}
# Output:  Minimum element is: 3
#               Maximum element is: 35
def minAndMaxElement(arr):

    minEle = arr[0]
    maxEle = arr[0]

    for i in range(1,len(arr)):
        if arr[i] > maxEle:
            maxEle = arr[i]

        if arr[i] < minEle:
            minEle = arr[i]

    print("Min and Max Elements in an array ",arr," is ",[minEle,maxEle])

if __name__ =="__main__":
    print("First Testcase")
    minAndMaxElement([3, 5, 4, 1, 9])
    print("Second Testcase")
    minAndMaxElement([22, 14, 8, 17, 35, 3])


