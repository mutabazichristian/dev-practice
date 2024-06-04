from typing import List
from collections import defaultdict

class Solution:
    def groudAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list) 
        result = []

        for s in str:
            sorted_s = tuple(sorted(s))
            anagram_map[sorted_s].append(s)