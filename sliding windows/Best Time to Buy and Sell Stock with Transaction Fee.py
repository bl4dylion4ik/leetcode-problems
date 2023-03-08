class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        s0 = 0
        s1 = -prices[0]
        for i in range(1, len(prices)):
            prev_s0 = s0
            s0 = max(s0, s1 + prices[i] - fee)
            s1 = max(s1, prev_s0 - prices[i])
        return s0