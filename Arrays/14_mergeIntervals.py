# Given an array of intervals where intervals[i] = [starti, endi],
# merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
#
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

def merge(arr):
    arr.sort(key=lambda x:x[0])
    idx = 0
    res = [arr[0]]
    for i in range(1,len(arr)):
        if res[idx][1] >= arr[i][0]:
            res[idx][1] = max(res[idx][1],arr[i][1])
        else:
            res.append(arr[i])
            idx = idx + 1

    print(res)
    
if __name__=="__main__":
    merge([[1,4],[0,2],[3,5]])



