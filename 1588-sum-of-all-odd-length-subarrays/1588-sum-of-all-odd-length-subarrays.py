class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # a=sum(arr)
        n=len(arr)
        # right=0
        # left=0
        # while right<n:
        sum_t=0
        for i in range(n):
            for j in range(i,n+1):
                if (j-i)%2!=0:
                    sum_t+=sum(arr[i:j])
        return sum_t
                    
            
            