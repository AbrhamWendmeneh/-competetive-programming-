class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        
        # nums.sort()
        graph={}
        
        set_val=sorted(list(set(nums)))
        
        for i, val in enumerate(set_val):
            if val not in graph:
                graph[val]=i

        counter=0            
        
        for i in range(len(nums)-1,-1,-1):
            
            counter += graph[nums[i]]
            
        return counter
            
