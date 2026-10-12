class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                substr = s[l:r + 1]
                l -= 1
                r += 1
            if len(substr) > len(longest):
                longest = s[l + 1:r]

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                substr = s[l:r + 1]
                l -= 1
                r += 1
            if len(substr) > len(longest):
                longest = s[l + 1:r]
        return longest

        


        