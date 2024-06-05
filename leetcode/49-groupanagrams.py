from collections import defaultdict
class Solution:
    def groupAnagram(self,strs):
        """
        :type strs: List[strs]
        :rtype: List[List[str]]
        """        
        anagram_map = defaultdict(list)
        for word in strs:
            anagram_map[tuple(sorted(word))].append(word)
            
        return anagram_map.values()
 