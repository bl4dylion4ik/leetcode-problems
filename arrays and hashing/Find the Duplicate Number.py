from typing import List


def findDuplicate(nums: List[int]) -> int:
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[slow]]

        if slow == fast:
            break

    slow = nums[0]