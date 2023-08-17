class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        current_sum = highest_sum = sum(nums[:k])
        for i in range(k,len(nums)):
            current_sum = current_sum - (nums[i-k]) + nums[i]
            if current_sum > highest_sum:
                highest_sum = current_sum
            
        return highest_sum /float(k)