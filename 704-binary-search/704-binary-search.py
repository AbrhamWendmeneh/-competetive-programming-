class Solution:
    def search(self, nums: List[int], target: int) -> int:
    
        left=0
        right=len(nums)-1
        while right>=left:
            middle=left+(right-left)//2
            if nums[middle]==target:
                return middle
            elif nums[middle]>target:
                right=middle-1
            else:
                left=middle+1
        return -1
                