class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""

        left = 0
        right = 0

        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            current = s[left + 1: right]
            if len(current) > len(longest):
                longest = current

            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            current = s[left + 1: right]
            if len(current) > len(longest):
                longest = current

        return longest
        




        