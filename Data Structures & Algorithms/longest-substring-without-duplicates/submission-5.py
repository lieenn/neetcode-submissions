class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        found = {}
        longest = 0

        left = 0
        streak = 0

        for right in range(len(s)):
            if s[right] in found:
                left = max(left, found[s[right]] + 1)
            found[s[right]] = right
            streak = right - left + 1
            longest = max(longest, streak)
        return longest
        