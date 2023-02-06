class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a=[]
        # b=[0:n]
        # c=[n:]
        for i in range(n):
            a.append(nums[i])
            a.append(nums[i+n])
        return a
        