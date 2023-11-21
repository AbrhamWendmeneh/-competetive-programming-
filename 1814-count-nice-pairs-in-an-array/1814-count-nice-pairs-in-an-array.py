class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        counter = 0
        diff_counts = {}

        for num in nums:
            diff = num - int(str(num)[::-1])

            if diff in diff_counts:
                counter += diff_counts[diff]
                diff_counts[diff] += 1
            else:
                diff_counts[diff] = 1

        return counter%((10**9)+7)
    
'''
I do this question by getting some hint from the question format in which 
it gives me some form of hint on how can I approach it, by the way I have do this question in brute force but it give me some TLE  case that's why I do like this
and I forget modulo
'''
                