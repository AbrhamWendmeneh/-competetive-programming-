class Solution:
    def numberOfWays(self, corridor: str) -> int:
        
        consq_s=0
        ways=0
        ans=1
        for i, val in enumerate(corridor):
            
            if val=='S':
                consq_s+=1
            
            if consq_s==2:
                ways+=1
              
            if consq_s==3:
                ans*=ways
                consq_s=1
                ways=0
                
        if consq_s < 2:
            return 0
        
        return ans%((10**9)+7)
                
                