class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # this code gives me time limit exceede for the last case 
        # # nums[-k:]+nums[:k+1]
        # temp=nums
        # for i in range(k%(len(nums))):
        #     val=temp.pop()
        #     temp=[val]+temp
        # nums[:]=temp
        
        
        #modfied version is 
        
        k=k%(len(nums))
        
        nums[:]=nums[-k:]+nums[:-k]
        
            
        
        