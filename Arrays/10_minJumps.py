# Given an array of integers where each element represents the max number of steps that can be made forward from that element.
# Write a function to return the minimum number of jumps to reach the end of the array
# (starting from the first element). If an element is 0, then we cannot move through that element. If we can’t reach the end, return -1.
#
# Input:  arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
# Output: 3 (1-> 3 -> 8 -> 9)
#
# Explanation: Jump from 1st element to
# 2nd element as there is only 1 step,
# now there are three options 5, 8 or 9.
# If 8 or 9 is chosen then the end node 9
# can be reached. So 3 jumps are made.

# python program to count Minimum number
# of jumps to reach end

# Returns minimum number of jumps to reach arr[n-1] from arr[0]
def minJumps(arr, n):
   n = len(arr)-1
   start = 0
   end = 0
   step = 0
   maxend = 0
   while end < n:
       step = step + 1
       for i in range(start,end+1):
           maxend = max(maxend,i +arr[i])
           if maxend >= n:
               return step

       start,end = end+1,maxend
   return step

if __name__=="__main__":
    arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    size = len(arr)

    print("Minimum number of jumps to reach end is % d " % minJumps(arr, size))











