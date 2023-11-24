class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        
        val_len= len(piles)//3
        
        result=0
        
        for i in range(len(piles)-2, val_len-1, -2):
            
            result += piles[i]
            
        return result
            
