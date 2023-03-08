def isHappy(n: int) -> bool:
    sums = 0
    while n > 0:
        r = n % 10
        sums = sums + r * r
        n = n // 10
    k = sums

    if k == 1:
        return True
    if k == 2 or k == 3 or k == 4:
        return False
    else:
        return isHappy(k)