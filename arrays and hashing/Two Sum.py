from typing import List


def twoSum( nums: List[int], target: int) -> List[int]:
    d = {}
    for i, j in enumerate(nums):
        r = target - j
        if r in d:
            return [d[r], i]
        d[j] = i