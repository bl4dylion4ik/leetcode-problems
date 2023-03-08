def isSubsequence(self, s: str, t: str) -> bool:
    for i in s:
        i = t.find(i)
        if i >= 0:
            t = t[i+1:]
        else:
            return False
    return True
