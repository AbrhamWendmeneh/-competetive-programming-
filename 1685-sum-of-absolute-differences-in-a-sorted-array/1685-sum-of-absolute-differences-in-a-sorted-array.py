class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        
        result=[]   
        
        suffix=sum(nums)
        
        prefix=0
        
        len_nums= len(nums)
        
        for i, val in enumerate(nums):
            
            prefix += val
            
            suffix -=val
            
            ans= (val*(i+1)-prefix) + abs(val*(len_nums-i-1)-suffix)
            
            result.append(ans)
            
        return result
       
        
        