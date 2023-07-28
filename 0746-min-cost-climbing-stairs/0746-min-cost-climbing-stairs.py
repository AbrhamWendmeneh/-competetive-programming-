class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def min_cost(i, memo):
            if i >= len(cost):
                return 0
            if i in memo:
                return memo[i]
            
            one_move=cost[i]+min_cost(i+1,memo)
            two_move=cost[i]+min_cost(i+2,memo)
            result=min(one_move,two_move)
            
            memo[i]= result
            return result
        return min(min_cost(0,{}),min_cost(1,{}))
        
            
        