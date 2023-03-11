# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
#
#   Open brackets must be closed by the same type of brackets.
#   Open brackets must be closed in the correct order.
#   Every close bracket has a corresponding open bracket of the same type.
#
# Input: s = "()"
# Output: true

class Solution:
    def isValid(self, s: str) -> bool:
        _map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in _map:
                stack.append(c)
                continue
            if not stack or stack[-1] != _map[c]:
                return False
            stack.pop()

        return not stack