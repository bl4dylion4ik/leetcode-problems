# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.
#
# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".


class Solution:

    def get_current_index(self, s, i):
        to_skip = 0

        while i >= 0:
            if s[i] == '#':
                to_skip += 1
            elif to_skip > 0:
                to_skip -= 1
            else:
                break
            i -= 1
        return i

    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s) - 1
        j = len(t) - 1

        while i >= 0 and j >= 0:
            i = self.get_current_index(s, i)
            j = self.get_current_index(t, j)

            if i < 0 or j < 0:
                return True
            if i < 0 or j < 0:
                return False
            if s[i] != t[j]:
                return False

            i -= 1
            j -= 1
        return True