# Longest consecutive subsequence
# Given an array of positive integers. Find the length of the longest
# sub-sequence such that elements
# in the subsequence are consecutive integers, the consecutive numbers can be in any order.
#
# Input:
# N = 7
# a[] = {2,6,1,9,4,5,3}
# Output:
# 6
# Explanation:
# The consecutive numbers here
# are 1, 2, 3, 4, 5, 6. These 6
# numbers form the longest consecutive
# subsquence.

def longestConsecutive(arr):
    arr.sort()
    Counter = 1
    curr_Counter = 1
    for i in range(1,len(arr)):
        if arr[i] == arr[i-1]+1:
            curr_Counter = curr_Counter + 1
            Counter = max(Counter,curr_Counter)
        else:
            curr_Counter = 1
            pass

    return Counter

if __name__=="__main__":
    print(longestConsecutive([-1,-2,0,1,2,4]))