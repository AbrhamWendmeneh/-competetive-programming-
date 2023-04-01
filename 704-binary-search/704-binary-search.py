class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''for i in range(len(nums)):
            if target==nums[i]:
                return i
        else:
            return -1'''
        low=0
        high=len(nums)-1
        
        while low<=high:
            
            mid=low+(high-low)//2
            
            if nums[mid]==target:
                
                return mid
            
            elif nums[mid]>target:
                
                high=mid-1
                
            else:
                
                low=mid+1
                
        # return low if low==high and nums[low]==target else  -1
        return -1
                