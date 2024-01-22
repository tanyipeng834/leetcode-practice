class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # Time complexity would be 9^k
        # Space complexity would be O(K) as the length of k determine the 
        # depth of recursion
        nums_array =[]
        def backtrack(number,num_array,start):
            # Edge case to return if the sum is more than n or the amount
            # of numbers is more than k
            if sum(num_array)>n or number>k:
                return
            elif sum(num_array) == n and number ==k:
                # Make a copy of the array
                nums_array.append(num_array[:]) 
            for i in range(start+1,10):
                # Try other combinations
                
                num_array.append(i)
                backtrack(number+1,num_array,i)
                # Pop element to backtrack
                num_array.pop()
        backtrack(0,[],0)
        return nums_array
            






        