from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    prefix = ""
    s = zip(*strs)
    for i in s:
        if len(set(i)) == 1:
            prefix += i[0]
        else:
            break
    return prefix