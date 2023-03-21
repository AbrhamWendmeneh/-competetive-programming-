class Solution:
    
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        '''res=0
        for i in range(1,max(nums)):
            for val in nums:
                  res+=math.ceil(val/i) 
        if res<=threshold:
            return i'''
        low=1
        # res=0
        high=max(nums)
        res=[]
    
        while low < high:
            
            mid=low+(high-low)//2
            
            for i in nums:
                
                # res=sum(i+mid-1)//
                res.append(math.ceil(i/mid))
                
            # print(res)    
            value=sum(res)
            
            
            if value > threshold:
                
                low=mid+1
                
            else:
                
                high=mid
            res=[]
                
        return low
    
        
        