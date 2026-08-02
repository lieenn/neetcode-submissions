class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        isAnagram = False

        for c in s:
            countS[c] = 1 + countS.get(c, 0)

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        for c in s:
            if c in countT and countS[c] == countT[c]:
                isAnagram = True
            else:
                return False

        return isAnagram