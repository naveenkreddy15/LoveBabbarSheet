# Given an array of positive and negative numbers, arrange them in an alternate fashion
# such that every positive number is followed by a negative and vice-versa maintaining
# the order of appearance. The number of positive and negative numbers need not be equal.
# If there are more positive numbers they appear at the end of the array.
# If there are more negative numbers,
# they too appear at the end of the array.

# Input:  arr[] = {1, 2, 3, -4, -1, 4}
# Output: arr[] = {-4, 1, -1, 2, 3, 4}
#
# Input:  arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
# Output: arr[] = {-5, 5, -2, 2, -8, 4, 7, 1, 8, 0}

def arrangeIntegers(arr):
    posIdx = 0
    negIdx = 0
    k = 0
    n = len(arr)

    while(posIdx < n and negIdx < n and k < n):
        if k%2 == 0:
            if(arr[k]<0):
                posIdx = k
                negIdx = k
                while(negIdx < n and arr[negIdx] < 0):
                    if(posIdx)


if __name__ == "__main__":
    print(arrangeIntegers([1, 2, 3, -4, -1, -4]))


