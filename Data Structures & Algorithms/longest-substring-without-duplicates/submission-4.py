class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        found = {}
        longest = 0

        left = 0
        for right in range(len(s)):
            if s[right] in found:
                left = max(left, found[s[right]] + 1)
            found[s[right]] = right
            length = right - left + 1
            longest = max(length, longest)
        return longest



