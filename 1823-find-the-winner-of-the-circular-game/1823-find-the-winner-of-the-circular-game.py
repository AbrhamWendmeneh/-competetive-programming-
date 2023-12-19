class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        array=[i+1 for i in range(n)]
        
        i=0
        
        while len(array)>1:
            
            i=(i+k-1)%(len(array))
            
            array.pop(i)

        return array[0]
    
# I did this when I attend my first assistance at A2SV 12/19/2023   
        