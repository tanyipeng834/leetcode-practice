class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # First find the max k
        max_pile  = max(piles)
        
        low = 1
        high = max_pile
        while low <= high:
            current_rate = (low+high)//2
           
            hours_needed =0

            for pile in piles:
                if pile%current_rate != 0:
                    hours_needed+= (pile//current_rate) +1
                else:
                    hours_needed += (pile//current_rate)
           
            if hours_needed<= h:
                high = current_rate -1
            else:
                low = current_rate +1
            hours_needed =0
        return low

            
