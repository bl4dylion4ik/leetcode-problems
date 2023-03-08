class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def generate(open_, close_, current):
            if open_ + close_ == 2 * n:
                result.append(current)
                return
            if open_ < n:
                generate(open_ + 1, close_, current + "(")
            if close_ < open_:
                generate(open_, close_ + 1, current + ")")

        generate(0, 0, "")

        return result