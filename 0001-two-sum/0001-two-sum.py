class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        store= {}
     
        for i,val in enumerate(nums):
            
            if target-val not in store: 
                store[val]=i
                
            else:
                return store[target-val],i
            
        