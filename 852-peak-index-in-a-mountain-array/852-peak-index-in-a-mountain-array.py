class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        '''res=0
        right=1
        left=0
        while right<len(arr) and right>left:
            
            if arr[right]>arr[left]:
                res=max(res,right)
                left+=1
                right+=1
            else:
                break
        return res'''
            
        low=0
        high=len(arr)-1
        target=max(arr)
        while low<high:
            mid=low+(high-low)//2
            
            if arr[mid+1]<arr[mid] and arr[mid-1]<arr[mid]:
                return mid
            elif arr[mid+1]>arr[mid]:
                low=mid+1
            else:
                high=mid-1
            '''
            if arr[mid+1]>arr[mid]:
                low=mid+1
            else:
                high=mid'''
        return low
                