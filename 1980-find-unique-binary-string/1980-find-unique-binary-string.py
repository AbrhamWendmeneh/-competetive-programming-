class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
       
        def helper(nums,n, current, result):
            
            if n==0:
                
                result.append(''.join(current))
                return 
            
            for char in ['0','1']:
                
                current.append(char)
                helper(nums, n - 1, current, result)
                current.pop()  
        
        dict_val={}
        
        for i in nums:
            
            dict_val[i]=1
            
        result=[]
        
        helper(nums, len(nums),[],result)
        
        
        for i in result:
            
            if i not in dict_val:
                
                return i
        
        