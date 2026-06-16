class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            pal = s[left + 1: right]
            if len(pal) > len(res):
                res = pal

            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            pal = s[left + 1: right]
            if len(pal) > len(res):
                res = pal

        return res

        




        