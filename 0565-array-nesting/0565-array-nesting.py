class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        
        max_val=float('-inf')
        visited=set()
        
        for num in nums:
            
            if num not in visited:
                count=0
                temp= num
                while temp not in visited:
                    visited.add(temp)
                    temp= nums[temp]
                    count+=1
                max_val= max(max_val, count)
        return max_val