# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low=1
        high=n
        ans=0
        while low<=high:
            mid=(low+high)//2
            if isBadVersion(mid):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        # print(isBadVersion(4))
        return ans
   