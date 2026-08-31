class Solution:
    def countSubstrings(self, s: str) -> int:
        l, r = 0, 0
        totalCount = 0

        for i in range(len(s)):
            # Odd length palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                totalCount += 1
                l -= 1
                r += 1

            # Even length palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                totalCount += 1
                l -= 1
                r += 1

        return totalCount