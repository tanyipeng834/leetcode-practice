class Solution:
    def rob(self, nums: List[int]) -> int:
        amount_of_money = nums.copy()
        # Looking in only the foward direction
        # The first house he can rob the next house
        for i in range(len(nums)-3,-1,-1):
            for j in range(i+2,len(nums)):
                # Check for the highest sum in the following houses
                if nums[i] + amount_of_money[j] > amount_of_money[i]:
                    amount_of_money[i] = nums[i] + amount_of_money[j]
                   
            
        return max(amount_of_money)