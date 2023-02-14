class Solution:
    def dividePlayers(self, nums: List[int]) -> int:
        nums.sort()
        a,b=nums[0], nums[-1]
        temp=sorted(nums)
        temp=temp[::-1]
        d=a+b
        c=0
        if len(nums)<4:
            return nums[0]*nums[1]
        for i in range(len(nums)//2):
            if nums[i]+temp[i]==d :
                
                
                c+=(nums[i]*temp[i])
            else:
                return -1
                break
        # if c<d and len(nums)>2:
        #     return -1
        return c