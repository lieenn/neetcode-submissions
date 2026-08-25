class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            pal_str = s[left + 1:right]
            if len(pal_str) > len(res):
                res = pal_str
            
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            pal_str = s[left + 1:right]
            if len(pal_str) > len(res):
                res = pal_str
        return res

            
        

        




        