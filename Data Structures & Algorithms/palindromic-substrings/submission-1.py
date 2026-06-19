class Solution:
    def countSubstrings(self, s: str) -> int:

        total = 0

        for i in range(len(s)):
            left, right = i, i
            length = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                length += 1
            total += length

            left, right = i, i + 1
            length = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                length += 1
            total += length
        return total
            
