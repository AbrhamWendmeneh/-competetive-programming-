class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        dict_val={}
        
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if (i+j) in dict_val:
         
                    dict_val[(i+j)].insert(0,nums[i][j])
                else:
                    dict_val[(i+j)]=[nums[i][j]]
                    

        result=[]
        for val in dict_val:
            result+=dict_val[val]
                    
        return result
                    