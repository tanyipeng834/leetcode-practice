class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows = [1] * n
        for row in range(m-1):
            newRow = [1] *n
            for col in range(n-2,-1,-1):
                newRow[col] = newRow[col+1] + rows[col]
            rows= newRow
        
        return rows[0]