class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        highest =0
        curr =0
        result_array =[0]
        for i in range(len(gain)):
           curr+=gain[i]
           highest = max(curr,highest)

        return highest