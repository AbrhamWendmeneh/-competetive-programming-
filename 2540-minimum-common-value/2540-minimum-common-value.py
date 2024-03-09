class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        set_val = set(nums1)

        counter = 0
        
        for i in nums2:
            
            if i in set_val:
                
                return i
        
        return -1
            