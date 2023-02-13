class Solution:
    def countOdds(self, low: int, high: int) -> int:
        a=0
        # for i in range(low,high+1):
        if  (low%2==1 or high%2==1 ):
            return (high-low)//2+1
        return (high-low)//2