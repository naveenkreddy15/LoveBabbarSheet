# Given an integer N, find its factorial.
#
# Input: N = 5
# Output: 120
# Explanation : 5! = 1*2*3*4*5 = 120
def factorial(n):
    res = 1
    for i in range(1,n+1):
        res = res * i

    return res

if __name__=="__main__":
    print(factorial(10))