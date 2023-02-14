class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        a=0
        counter=0
        nums.sort()
        b=len(nums)-1
        while a< b:
            if nums[a]+nums[b]<k:
                a+=1
            elif nums[a]+nums[b]>k:
                b-=1
            else:
                a+=1
                b-=1
                counter+=1
        return counter
                
                    