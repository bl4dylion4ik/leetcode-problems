def lengthOfLongestSubstring(s: str) -> int:
    seen = {}
    l = 0
    r = 0
    output = 0

    while r < len(s):
        if s[r] not in seen:
            output = max(output, r - l + 1)

        elif seen[s[r]] < l:
            output = max(output, r - l + 1)

        else:
            l = seen[s[r]] + 1
        seen[s[r]] = r
        r += 1
    return output

