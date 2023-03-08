from typing import List


def peakIndexInMountainArray(arr: List[int]) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = left + (right-left) // 2

        if arr[middle] < arr[middle + 1]:
            left = middle + 1
        else:
            right = middle - 1
    return left

