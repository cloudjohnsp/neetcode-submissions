class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        l, r = 0, 1
        while r <= len(s)-1:
            leftSum = ord(s[l])
            rightSum = ord(s[r])
            print(rightSum, '-', leftSum)
            score += abs(rightSum - leftSum)
            print('score: ',score)
            r += 1
            l += 1
        return score