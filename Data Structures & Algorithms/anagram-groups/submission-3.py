class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for i in strs:
            char_pos = [0]*26
            for j in i:
                char_pos[ord(j)-ord('a')] += 1
            anagrams[tuple(char_pos)].append(i)        
        return list(anagrams.values())
            