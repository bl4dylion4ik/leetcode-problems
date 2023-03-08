from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    nums_set = set(nums)
    print(nums_set)
    return not len(nums) == len(nums_set)


print(containsDuplicate([1,2,3,1]))