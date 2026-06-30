class Solution:
    def countSubstrings(self, s: str) -> int:

        total = 0

        l, r = 0, 0

        for i in range(len(s)):
            l, r = i, i
            length = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length += 1
                l -= 1
                r += 1
            total += length

        for i in range(len(s)):
            l, r = i, i + 1
            length = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length += 1
                l -= 1
                r += 1
            total += length

        return total

            
