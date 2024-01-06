class SmallestInfiniteSet:


    def __init__(self):
        self.nums = []
        for i in range(1,1001):
            self.nums.append(i)
        heapq.heapify(self.nums)
        
        





        

    def popSmallest(self) -> int:
        # Return the smallest in a o(1) time complexity
        return heapq.heappop(self.nums)
        

    def addBack(self, num: int) -> None:
        if num not in self.nums:
            heapq.heappush(self.nums,num)
        
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)