# Maximum profit by buying and selling a share at most twice
#
# In daily share trading, a buyer buys shares in the morning and sells them on the same day.
# If the trader is allowed to make at most 2 transactions in a day,
# whereas the second transaction can only start after the first one is complete
# (Buy->sell->Buy->sell). Given stock prices throughout the day,
# find out the maximum profit that a share trader could have made.
#
# Input:   price[] = {10, 22, 5, 75, 65, 80}
# Output:  87
# Trader earns 87 as sum of 12, 75
# Buy at 10, sell at 22,
# Buy at 5 and sell at 80
#
# Input:   price[] = {2, 30, 15, 10, 8, 25, 80}
# Output:  100
# Trader earns 100 as sum of 28 and 72
# Buy at price 2, sell at 30, buy at 8 and sell at 80
import sys


def maxProfit(arr):
    currProfit = arr[0]
    maxProfit = -sys.maxsize
    totalProfit = 0

    for i in range(1,len(arr)):
        currProfit = currProfit - arr[i]
        if (currProfit > maxProfit):
            maxProfit = currProfit

        if (currProfit <= 0):
            currProfit = 0

    return maxProfit
if __name__=="__main__":
    print(maxProfit([2, 30, 15, 10, 8, 25, 40]))
