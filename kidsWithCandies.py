class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        return_list =[]
        for candy in candies:
            if candy + extraCandies >=max(candies):
                return_list.append(True)
            else:
                return_list.append(False)

        return return_list