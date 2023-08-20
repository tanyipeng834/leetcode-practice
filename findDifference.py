class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        nums1_array =[]
        for element in nums1_set:
            if element in nums2_set:
                
                nums2_set.remove(element)
            else:
                nums1_array.append(element)
        return [nums1_array,list(nums2_set)]
