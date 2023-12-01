class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        result=0
        left, right= 0, 1
        
        while right< len(prices):
            
            if prices[right] > prices[left]:
                result+= prices[right]-prices[left]
                
            left+=1              
            right+=1
            
        return result