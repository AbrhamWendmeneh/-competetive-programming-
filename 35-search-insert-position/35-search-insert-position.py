class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        right=len(nums)-1
        left=0
        while right>=left:
            middle = left+(right-left)//2
            if nums[middle]==target:
                return middle
            elif nums[middle]>target:
                right=middle-1
            else:
                left=middle+1
        return left
        
        
                
        
        