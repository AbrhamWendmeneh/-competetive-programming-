class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo={}
        def dp(amount):
            val=float("inf")

            if amount ==0:
                return 0
            if amount< 0:
                return val
            if amount in memo:
                return memo[amount]
            for i in coins:
                val=min(dp(amount-i)+1,val)
            memo[amount]=val
            
            return memo[amount]
        if dp(amount)< float('inf'):
            return dp(amount)
        return -1
            
                