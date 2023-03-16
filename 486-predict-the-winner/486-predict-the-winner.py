class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        array =[[0]*len(nums) for _ in range(len(nums))]
		
        for i in range(len(nums)-1,-1,-1):
            for j in range(i,len(nums)):
                if i==j:
                    array[i][j] = nums[i]
                else:
                    array[i][j] = max(nums[i] - array[i + 1][j], nums[j] - array[i][j - 1])
                    
        return array[0][-1]>=0