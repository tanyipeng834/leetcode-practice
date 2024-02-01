class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # created a classic dp_array to keep the profit from each transaction
        # We will do the dp problem with the top up approach
        # The row would be the buy price
        # The column would be the sell price
    
        buy = float('-inf')
        sell =0
        for price in prices:
            buy = max(buy,sell-price)
            sell = max(sell,buy+price-fee)
        return sell