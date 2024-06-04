from collections import defaultdict

class Solution(object):
    def containsDuplicate(self,num):
        """
        
        :type nums: List[int]
        :rtype:bool
        """
        duplicate_map = defaultdict(list)

        for n in num:
            duplicate_map[n].append(n)

        for value in duplicate_map.values():
            if len(value) > 1:
                return True
        
        return False