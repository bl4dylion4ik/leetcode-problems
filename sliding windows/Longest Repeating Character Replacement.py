def characterReplacement(s: str, k: int) -> int:
    l = 0
    r = 0
    output = 0
    past_value = 0

    count_k = 0

    while r < len(s):
        if s[r] == s[l]:
            output = max(output, r - l + 1)
        elif s[r] != s[l]:
            if count_k < k:
                output = max(output, r - l + 1)
                if count_k == 0:
                    past_value = r
                count_k += 1
            elif k == 0:
                l = r
                count_k = 0
            else:
                l = past_value - 1
                count_k = 0
        r += 1
    return output


characterReplacement("AABABBA", 1)