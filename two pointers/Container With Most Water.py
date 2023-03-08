# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
#
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
# In this case, the max area of water (blue section) the container can contain is 49.
#
# We take two pointers the beginning and the end of the array,
# We consider the volume which is equal to the distance between the pointers multiplied by the smallest height of the pointer
# We compare the resulting volume with the maximum. If it is larger, then we update the maximum.
# Next, if the height of the left pointer is less than the right one, then we move the left pointer, if the height is greater, then we move the right one
#
# [1,8,6,2,5,4,8,3,7]
#
# l                r  area=1*8=8  max_area=8
#   l              r  area=7*7=7  max_area=49
#   l             r   area=3*6=18 max_area=49
# ...continue
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            max_area = max(max_area, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area