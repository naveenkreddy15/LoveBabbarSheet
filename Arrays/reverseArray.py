# Write a program to reverse an array or string

def reverseArray(arr):
    res = []

    for i in reversed(arr):
        res.append(i)

    print("reversing the array using reversed function ",res)

    i = 0
    j = len(arr)-1

    while i < j:
        arr[i],arr[j] = arr[j],arr[i]
        i = i + 1
        j = j - 1

    print("revering the array using loop",arr)


if __name__=="__main__":
    reverseArray([1,4,2,3,5,7])


