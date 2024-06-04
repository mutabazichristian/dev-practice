class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums:List[int]
        :type target: int
        :rtype: List[int]
        """

        i = 0
        for i in range(len(nums)):
            for p in range(i+1, len(nums)):
                if (target - nums[i] == nums[p]):
                    return [i, p]
