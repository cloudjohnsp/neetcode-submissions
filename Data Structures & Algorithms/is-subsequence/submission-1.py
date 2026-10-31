class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        l = 0
        for r in t:
            if l == len(s)-1:
                return True
            if s[l] == r:
                l += 1
        return False