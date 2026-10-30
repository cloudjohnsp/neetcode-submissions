class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l <= r:
            lowered_left, lowered_right = s[l].lower(), s[r].lower()
            if not lowered_left.isalnum():
                l += 1
            elif not lowered_right.isalnum():
                r -= 1
            elif lowered_left != lowered_right:
                return False
            else:
                l += 1
                r -= 1
        return True