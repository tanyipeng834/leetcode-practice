class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        We can reduce this problem to the following subproblems
        - creating, pushing and popping from a min heap
        - traversing an array using a single pointer
        - modifying an array in place
        '''

        nums = [(-1 * num) for num in nums]
        heapq.heapify(nums)
        while k > 1:
            heapq.heappop(nums)
            k -= 1

        return -1 * nums[0]
