from collections import Counter

def checkInclusion(s1: str, s2: str) -> bool:
    len_s1 = len(s1)
    s1_counter = Counter(s1)
    window_counter = Counter()

    for i, c in enumerate(s2):
        window_counter[c] += 1

        if i >= len_s1:
            elem = s2[i - len_s1]
            if window_counter[elem] == 1:
                del window_counter[elem]
            else:
                window_counter[elem] -= 1

        if window_counter == s1_counter:
            return True
    return False