class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        # Space Comlexity would be O(1)
        # Time Complexity would be O(n)
        for i in range(len(cost)-3,-1,-1):
            cost[i] = min(cost[i+1]+cost[i],cost[i+2]+cost[i])
        return min(cost[0],cost[1])