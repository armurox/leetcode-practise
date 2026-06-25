class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = prices[0]
        max_profit = 0
        for elem in prices[1:]:
            if elem < curr_min:
                curr_min = elem
            else:
                max_profit = max(elem - curr_min, max_profit)
        return max_profit