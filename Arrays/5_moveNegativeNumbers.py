# Move all negative numbers to beginning and positive to end with constant extra space
#
# An array contains both positive and negative numbers in random order.Rearrange the array elements so that all negative numbers appear before all positive numbers.
#
# input: -12, 11, -13, -5, 6, -7, 5, -3, -6
# Output: -12 -13 -5 -7 -3 -6 11 6 5

def moveNegative(arr):
    j = 0

    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i],arr[j] = arr[j],arr[i]
            j = j + 1


    print("resultant array is ",arr)

if __name__ == "__main__":
    print("First testcase")
    moveNegative([-12, 11, -13, -5, 6, -7, 5, -3, -6])
    print("second testcase")
    moveNegative([1, 2,  -4, -5, 2, -7, 3, 2, -6, -8, -9, 3, 2,  1])

