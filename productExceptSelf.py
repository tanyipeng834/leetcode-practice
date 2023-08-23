class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result_list=[]
        # This is for the prefix list
        for i in range(len(nums)):
            if i ==0:
                result_list.append(1)
            else:
                result_list.append(nums[i-1]*result_list[i-1])
        
        post =1
        for j in range(len(nums)-1,0,-1):
            
    
            post *= nums[j]
            result_list[j-1] = result_list[j-1] * post
                
        return result_list