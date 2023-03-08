from typing import List


def singleNumber(nums: List[int]) -> int:
    mask = 0

    for i in nums:
        mask ^= i

    return mask