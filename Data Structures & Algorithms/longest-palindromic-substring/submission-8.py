class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            l, r = i, i
            length = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            pal = s[l + 1:r]
            if len(pal) > len(longest):
                longest = pal

            l, r = i, i + 1
            length = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            pal = s[l + 1:r]
            if len(pal) > len(longest):
                longest = pal

        return longest