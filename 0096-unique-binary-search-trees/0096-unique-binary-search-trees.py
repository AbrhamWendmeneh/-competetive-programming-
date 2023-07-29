class Solution:
    def numTrees(self, n: int) -> int:
        memo={}
        def dp(n):
            res=0
            if n<=1:
                return 1
            if n in memo:
                return memo[n]
            for i in range(n):
            # left subtree (nodes 0 to i-1) and right subtree (nodes i+1 to n-1)
                res+=dp(i)*dp(n-i-1)
            memo[n]=res
            
            return res
        
        return dp(n)