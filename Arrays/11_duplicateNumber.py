# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
#
# There is only one repeated number in nums, return this repeated number.
#
# You must solve the problem without modifying the array nums and uses only constant extra space.
#
# Input: nums = [1,3,4,2,2]
# Output: 2
#
# Input: nums = [3,1,3,4,2]
# Output: 3

def findDuplicate(arr):
    from collections import Counter
    nums_dict = Counter(arr)
    duplicateEle = list(nums_dict.most_common()[0])
    print("Duplicate number in an arr is ",duplicateEle[0])

    #Another version of finding the duplicate element
    print("Another version of finding the duplicate value in an arr is",max(zip(nums_dict.values(),nums_dict.keys()))[1])

if __name__ =="__main__":
    findDuplicate([1,3,4,2,2])



