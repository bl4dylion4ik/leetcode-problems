from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        sums = []

        curSum = 0
        for i in nums:
            curSum += i
            sums.append(curSum)

        self.sums = sums

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sums[right]
        return self.sums[right] - self.sums[left - 1]