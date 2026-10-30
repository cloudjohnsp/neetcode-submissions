class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i in strs:
            char_pos = [0]*26
            for j in i:
                char_pos[ord(j)-ord('a')] += 1
            if tuple(char_pos) not in anagrams:
                anagrams[tuple(char_pos)] = [i]
            else:
                anagrams[tuple(char_pos)].append(i)
        result = []
        for i in anagrams.values():
            result.append(i)
        return result
            