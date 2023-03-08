# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
#
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# We take two pointers, the left equal to the first and the right equal to the last element.
# Compare the squares of the numbers. If the square of the left pointer is larger than the square of the right,
# then add the square of the left pointer to the end of the new array and move the left pointer,
# if the square of the right is larger, then we divide the opposite.
# [-4,-1,0,3,10]    result=[0,0,0,0,0]
#  l          r     -4**2<10**2  result=[0,0,0,0,100]
#  l         r      -4**2>3**2   result = [0, 0, 0, 16, 100]
#      l     r      -1**2<3**2   result = [0, 0, 9, 16, 100]
# ...continue
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 0
        right = n - 1

        result = [0 for _ in range(n)]

        for i in range(n - 1, -1, -1):
            if nums[left] ** 2 > nums[right] ** 2:
                result[i] = nums[left] ** 2
                left += 1

            else:
                result[i] = nums[right] ** 2
                right -= 1

        return result