#
# https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
#
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        idx = 0
        profit = 0
        while idx < len(prices) - 1:
            idx+=1
            if prices[idx] > prices[idx + 1]:
                continue
            profit += prices[idx + 1] - prices[idx]
        return profit
