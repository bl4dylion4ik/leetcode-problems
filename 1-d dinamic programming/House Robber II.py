class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        n = len(nums)

        dp1 = [0] * (n + 1)
        for i in range(2, n + 1):
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i - 2])

        dp2 = [0] * (n + 2)
        for i in range(3, n + 2):
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i - 2])

        return max(dp1[-1], dp2[-1])