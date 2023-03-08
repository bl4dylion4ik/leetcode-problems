# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
#
# Return the sum of the three integers.
#
# You may assume that each input would have exactly one solution.

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# This problem is solved with the help of two pointers. At the beginning we sort the array.
# Next, we go in a loop along i from the beginning of the array to the len(nums) element.
# Fix the left pointer as i+1 and the right pointer as len(nums).
# Then we count the sum of all the numbers (nums[i]+nums[right]+nums[left].
# If the absolute difference between the target and the nearest amount is greater than the absolute difference
# between the target and the calculated amount, then the nearest amount is equal to the calculated amount.
# Next, if the calculated amount is less than the target, we move the left pointer, if the amount is greater, we move the right pointer

# Example nums = [-1,2,1,-4], target = 1
#                 [-4,-1,1,2]
#                 i    l    r  total=-4-1+2=-3, closest_sum=-3, total<target l+=1
#                 i      l  r  total=-4+1+2=-1, closest_sum=-1, total<target l+=1 l==r, so i+=1
#                      i l  r  total=-1+1+2=2, closest_sum=2, total>target r-=1 l==r, so i+=1 end of the loop

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest_sum = float('inf')
        nums.sort()
        for i in range(len(nums) - 2):
            if nums[i] == nums[i + 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == target:
                    return total
                if abs(target - closest_sum) > abs(target - total):
                    closest_sum = total

                if total < target:
                    left += 1
                else:
                    right -= 1

        return closest_sum
