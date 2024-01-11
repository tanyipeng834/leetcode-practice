class Solution:
    def guessNumber(self, n: int) -> int:
        low ,high = 1 ,n
        result = -2
        while result != 0:
            mid = (low + high)//2
            result = guess(mid)
           
            if result ==-1:
                high = mid -1 
            elif result ==1 :
                low = mid +1
        return mid


