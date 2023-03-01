class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # [k:]+[0:k-1]
        # nums[:]=nums[k+1:]+nums[0:k+1]
        k=k%len(nums)
        nums[:]=nums[-k:]+nums[0:-k]
        