class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        end = len(height)-1
        start =0
        max_water =0
        # Take the case where 
        while end>start:
            if height[start]<=height[end]:
                max_water = max(max_water,(end-start)*height[start])
                start+=1
            else:
                max_water = max(max_water,(end-start)*height[end])

                end-=1
        return max_water
