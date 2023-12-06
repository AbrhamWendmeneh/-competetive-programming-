class Solution:
    def totalMoney(self, n: int) -> int:
        
        temp= n
        
        base_money=1
        
        result=0
        
        for i in range(temp//7):
            
            result+= sum(range(base_money, base_money+7))
            
            base_money+=1
            
        result+= sum(range(base_money, base_money+ temp%7))
        
        return result