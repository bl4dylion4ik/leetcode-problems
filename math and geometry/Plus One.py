from typing import List


def plusOne(digits: List[int]) -> List[int]:
    if digits[-1] != 9:
        digits[-1] += 1
        return digits
    n = len(digits) - 1
    while digits[n] == 9:
        digits[n] = 0
        n -= 1
    if n < 0:
        digits.insert(0, 1)
        return digits
    digits[n] += 1

    return digits

print(plusOne([8, 9, 9,9]))