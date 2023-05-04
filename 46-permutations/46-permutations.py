class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
      
        res = []

        def backtrack(nums, path, res):
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                backtrack(nums[:i]+nums[i+1:], path+[nums[i]], res)
        backtrack(nums, [], res)
        return res
    
    '''
    The backtrack function takes three arguments: the remaining numbers to be permuted (nums), the current              permutation (path), and the result list (res). If there are no more numbers left to pick, we can add the current        permutation to the result list. Otherwise, we iterate through the remaining numbers and recursively call                backtrack with the ith number removed from nums and added to path.
    '''
    
    