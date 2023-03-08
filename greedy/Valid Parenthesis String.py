class Solution:
    def checkValidString(self, s: str) -> bool:
        left_min, left_max = 0, 0

        for c in s:
            if c == "(":
                left_min, left_max = left_min + 1, left_max + 1
            elif c == ")":
                left_min, left_max = left_min - 1, left_max - 1
            else:
                left_min, left_max = left_min - 1, left_max + 1
            if left_max < 0:
                return False
            if left_min < 0:
                left_min = 0

        return left_min == 0


####################

class Solution:
    def checkValidString(self, s: str) -> bool:
        stack, star = [], []

        for i,char in enumerate(s):
            if char == "(": stack.append(i)
            elif char == ")":
                if not stack and not star: return False
                elif stack: stack.pop()
                elif star: star.pop()
            else: star.append(i)

        while stack:
            if star and stack[-1] < star[-1]:
                stack.pop()
                star.pop()
            else:
                if not star: return False
                else: star.pop()

        return True