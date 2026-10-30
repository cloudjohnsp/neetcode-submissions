class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) or s == '' or t == '':
            return False

        common_len = len(s)
        occurrences = [0]*26

        for i in range(common_len):
            curr_s = ord(s[i]) - ord('a')
            occurrences[curr_s] += 1
            curr_t = ord(t[i]) - ord('a')
            occurrences[curr_t] -= 1

        for i in occurrences:
            if i != 0:
                return False

        return True
        
        