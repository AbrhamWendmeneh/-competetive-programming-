class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        if n==1:
            return '0'
        res='011'
        i=2
        while i <n:
            
            res=res+'1'+res[:int(len(res)/2)]+'0'+res[int(len(res)/2)+1:]
            
            i+=1
            
        return res[k-1]