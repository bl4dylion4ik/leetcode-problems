from typing import List


def countBits(n: int) -> List[int]:
    memo = [0] * (n + 1)

    for i in range(1, n + 1):
        memo[i] = memo[i >> 1] + i % 2

    print(memo)
    return memo[:n + 1]