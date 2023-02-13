class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # a=[]
        # for i in nums1:
        #     a.append(i)
        # for j in nums2:
        #     a.append(j)
        a=nums1+nums2
        a.sort()
        if len(a)%2!=0:
            return a[((len(a)+1)//2)-1]
        else:
            return (a[(len(a)//2)-1]+a[(len(a)//2)])/2