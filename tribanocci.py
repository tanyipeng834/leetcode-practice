class Solution:
    # With memoization, we managed to reduce the time complexity of this code
    # from O(3^n) to O(n)
    # However, we increase the space complexity from O(1) to O(n) which
    # is still acceptable
    def tribonacci(self, n: int) -> int:
        def fib(n):
            if n ==0:
                return 0
            if n ==1 or n==2:
                return 1
            # Given the case where the result has been stored
            elif dp[n]!=-1:
                return dp[n]
            # Memoiza the results
            dp[n] = fib(n-3)+fib(n-2)+fib(n-1)
            return dp[n]
        dp =[-1] *(n+1)
        a= fib(n)
        return (a)
