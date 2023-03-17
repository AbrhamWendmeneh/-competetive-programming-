class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''if target in nums:
            return nums.index(target)
        return -1'''
        right=len(nums)-1
        left=0
        if len(nums)==1 and nums[0]!=target:
            return -1
            
        while left<=right:
            mid=(right+left)//2
            if nums[mid]==target:
                return mid
            elif (nums[mid]-nums[left])>=0:
                if (nums[mid]>=target) and (nums[left]<=target):
                    right=mid-1
                
                else:
                    left=mid+1
            else:
                if (target>nums[mid]) and (target<=nums[right]):
                    left=mid+1
                else:
                    right=mid-1
        return -1
                    
                