from typing import List


def maxSubArray(nums: List[int]) -> int:
    max_sub = nums[0]
    currSum = 0

    for i in nums:
        if currSum < 0:
            currSum = 0

        currSum += i
        max_sub = max(max_sub, currSum)
    return max_sub