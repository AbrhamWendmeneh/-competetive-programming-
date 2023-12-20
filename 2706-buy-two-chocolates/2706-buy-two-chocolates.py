class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        
        prices.sort()
        
        sum_val = sum(prices[0:2])
        
        if money - sum_val >=0:
            
            return money - sum_val
        
        else:
            
            return money 
        
        
            