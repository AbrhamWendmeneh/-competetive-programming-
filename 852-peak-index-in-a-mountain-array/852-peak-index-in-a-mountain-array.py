class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        res=0
        right=1
        left=0
        while right<len(arr) and right>left:
            
            if arr[right]>arr[left]:
                res=max(res,right)
                left+=1
                right+=1
            else:
                break
        return res
            