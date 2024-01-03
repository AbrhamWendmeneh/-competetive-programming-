class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        result = 0
        counter = 0
        new_bank = []
        
        for i,val in enumerate(bank):
            
            if val.count('1') > 0:
                
                new_bank.append(val)
        
        for j in range(1,len(new_bank)):
            
            val1 = new_bank[j].count('1')
            
            val2 = new_bank[j-1].count('1')    
                
            result += val1 * val2
                
        return result
            
            
            
            