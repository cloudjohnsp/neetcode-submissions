class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        count = set()
        l, r, max_count = 0, 0, 1
        while l <= r and r < len(s):
            if s[r] not in count:
                count.add(s[r])
                r += 1
                max_count = max(len(count), max_count)
            else:
                count.remove(s[l])
                l += 1

        return max_count