class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """

    def length_of_longest_substring_k_distinct(self, s: str, k: int) -> int:
        # write your code here
        left = 0

        result = 0
        counter = defaultdict(int)

        for right in range(len(s)):
            counter[s[right]] += 1

            while len(counter) > k:
                left_char = s[left]
                counter[left_char] -= 1
                if counter[left_char] == 0:
                    del counter[left_char]
                left += 1
            result = max(result, right - left + 1)

        return result