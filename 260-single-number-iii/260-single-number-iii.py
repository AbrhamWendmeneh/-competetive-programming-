class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        val=0
        for i in nums:
            val^=i
            
        #I use this as filtter
        # num & (1<< shift)
        newVal=  val & ~(val-1)
        # newVal=
        # print(newVal)
        
        res1=0
        res2=0
        for i in range(len(nums)):
            #to filter values using the above condition
            if nums[i] & newVal==0:
                
                res1^=nums[i]
                # print(res1)
            # for the values    
            else:
                
                res2^=nums[i]
                print(res2)
        return [res1,res2]
                
            
            
            
            
