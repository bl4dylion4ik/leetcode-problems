from typing import List


def replaceElements(arr: List[int]) -> List[int]:
    len_arr = len(arr)
    max_val = arr[len_arr-1]
    prev_val = arr[len_arr-1]
    if len_arr == 1:
        return [-1]
    for i in range(len_arr-1, -1, -1):
        if prev_val >= max_val:
            max_val = prev_val
        prev_val = arr[i]

        arr[i] = max_val

    arr[len_arr-1] = -1
    return arr

replaceElements([17,18,5,4,6,1])