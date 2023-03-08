from typing import List
from functools import reduce


def productExceptSelf(nums: List[int]) -> List[int]:
    res = [1] * len(nums)
    product = 1
    for i, num in enumerate(nums):
        res[i] *= product
        product *= num
    print(res)

    product = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= product
        product *= nums[i]
    return res



nums = [1,2,3,4]
res = [1]*len(nums)
product =1
for i, num in enumerate(nums):
    res[i] *= product
    product *= num
print(res)

product = 1
for i in range(len(nums) - 1, -1, -1):
    res[i] *= product
    product *= nums[i]