class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        field_one = []
        
        field_two = []
        
        for i in nums:
            
            if i > 0:
                
                field_one.append(i)
                
            else:
                
                field_two.append(i)
                
        result = []
        
        for i in range(len(nums)//2):
            
            result.append(field_one[i])
            
            result.append(field_two[i])
            
        return result
                
                
        