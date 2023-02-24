class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
#         if len(nums)==1 and  nums[0]!=k:
            
#             return 0
        #bruteforce for this question
        #but time limit exceeded for this code and I try to optimize it                 with linear time complexity using prefix sum
        # counter=0
        # for i in range(len(nums)):
        #     sumt=0
        #     for j in range(i,len(nums)):
        #         sumt+=nums[j]
        #         if sumt%k==0:
        #             counter+=1
        # return counter
        res = {0: 1}
        prefSum = 0
        count = 0
        for i in range(len(nums)):
            prefSum = (prefSum + nums[i]) % k
            if prefSum < 0:
                prefSum += k
            if prefSum in res:
                count += res[prefSum]
            if prefSum not in res:
                res[prefSum] = 0
            res[prefSum] += 1
        return count
            