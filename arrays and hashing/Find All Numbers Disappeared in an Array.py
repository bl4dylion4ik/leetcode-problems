from typing import List


def findDisappearedNumbers(nums: List[int]) -> List[int]:
    i = 0
    while i < len(nums):
        pos = nums[i] - 1
        if nums[pos] != nums[i]:
            nums[pos], nums[i] = nums[i], nums[pos]
        else:
            i += 1

    miss = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            miss.append(i + 1)
    return miss