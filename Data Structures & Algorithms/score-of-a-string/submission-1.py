class Solution:
    def scoreOfString(self, s: str) -> int:
        score, l, r = 0, 0, 1
        while r <= len(s)-1:
            score += abs(ord(s[r]) - ord(s[l]))
            r += 1
            l += 1
        return score