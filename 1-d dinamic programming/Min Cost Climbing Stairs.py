class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost[0], cost[1])

        cost.append(0)

        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])



######################

class Solution:
	def minCostClimbingStairs(self, cost: List[int]) -> int:
		cur = 0
		dp0 = cost[0]
		if len(cost) >= 2:
			dp1 = cost[1]

		for i in range(2, len(cost)):
			cur = cost[i] + min(dp0, dp1)
			dp0 = dp1
			dp1 = cur

		return min(dp0, dp1)