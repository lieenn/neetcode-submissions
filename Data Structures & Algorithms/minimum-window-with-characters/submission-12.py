class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countS, countT = {}, {}
        substrLen, substrInd = float('inf'), [-1, -1]

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        l = 0
        have, need = 0, len(countT)
        for r in range(len(s)):
            countS[s[r]] = 1 + countS.get(s[r], 0)
            if s[r] in countT and countT[s[r]] == countS[s[r]]:
                have += 1

            while have == need:
                if (r - l + 1) < substrLen:
                    substrLen = (r - l + 1)
                    substrInd = [l, r]
                if s[l] in countT and countT[s[l]] == countS[s[l]]:
                    have -= 1
                countS[s[l]] -= 1
                l += 1
        l, r = substrInd
        return s[l:r+1] if substrLen != float('inf') else ""

