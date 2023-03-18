class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left= 1
        right=max(piles)
        min_val = right
        while left <= right:
            mid = left+(right-left) // 2
            hour = 0
            for i in piles:
                hour += ceil(i/mid)
            if hour <= h:
                min_val = min(min_val,mid)
                right = mid-1
            else:
                left = mid+1
        return min_val