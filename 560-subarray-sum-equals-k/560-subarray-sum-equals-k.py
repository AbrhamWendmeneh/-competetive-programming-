class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0

        prefix = 0

        count = Counter({0: 1})

        for num in nums:

            prefix += num

            ans += count[prefix - k]

            count[prefix] += 1

        return ans
    
    '''
    
    nums = [1,1,1], k = 2
    
    
    count={0:1}
    nums=[1,5,2,4,3,3,4,6] k=6
    count={0:1,1:1,6:1,8:1,12:1,15:18:1,22:1,28:1}
    nums=[1,0,-1,1,0,0,2,-1] k=1
    count={0:1,1:1,1:2,0:2,1:3,1:4,1:5,3:1,2:1,}
    ans=1,2,4,6,8,13
    
    '''