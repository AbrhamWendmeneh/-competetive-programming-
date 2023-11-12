class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        # counter={}
        # for i in range(k+1):
        #     counter[i+1]=0
        # i= len(nums)-1
        
        collector=[]
        i=len(nums)-1
        
        while i >=0:
            
            if nums[i]<= k and nums[i] not in collector:
                
                collector.append(nums[i])
                
                if len(collector)==k:
                    
                    return len(nums)-i   
                
            i-=1
            