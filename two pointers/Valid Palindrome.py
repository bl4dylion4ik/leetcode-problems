# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
# non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# We remove unnecessary characters and bring them to lowercase
# Then we take two pointers, the left one is equal to the first value and the right one is equal to the last one.
# Compare these two values if they are equal, shift, if not, then the string is not a palindrome

# amanaplanacanalpanama
#
# i                   r  a==a
#  i                 r  m==m
#   i               r  a==a
#    i             r  n==n
#
# ... continue
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = self.helper(s)

        l, r = 0, len(clean_str) - 1

        while l < r:
            if clean_str[l] != clean_str[r]:
                return False

            l += 1
            r -= 1
        return True

    def helper(self, s: str) -> str:
        return ''.join(ch.lower() for ch in s if ch.isalnum())