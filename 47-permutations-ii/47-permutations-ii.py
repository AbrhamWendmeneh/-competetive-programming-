class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(nums, path, res):
            
            if not nums:
                
                res.append(path)
                
            for i in range(len(nums)):
                
                backtrack(nums[:i]+nums[i+1:], path+[nums[i]], res)
                
        backtrack(nums, [], res)
        
        final_val=[]
        
        for i in res:
            
            if i not in final_val:
                
                final_val.append(i)
                
        return final_val