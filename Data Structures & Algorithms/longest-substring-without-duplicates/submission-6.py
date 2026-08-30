class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        found = {}
        longest = 0

        length = 0
        l = 0
        for r in range(len(s)):
            if s[r] in found:
                l = max(l, found[s[r]] + 1)
            found[s[r]] = r
            length = r - l + 1
            longest = max(longest, length)
        return longest

            
