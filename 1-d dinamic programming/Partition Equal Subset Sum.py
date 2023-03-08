class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False

        total_sm = sum(nums)
        if total_sm % 2 != 0:
            return False

        total = total_sm // 2
        res = {0}

        for i in range(len(nums) - 1, -1, -1):
            for x in res.copy():
                sm = x + nums[i]
                if sm == total and total in res:
                    return True
                res.add(sm)
        return False