class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a=[]
        for i in list(set(nums1)):
            if i not in list(set(nums2)):
                a.append(i)
        b=[]        
        for j in list(set(nums2)):
            if j not in list(set(nums1)):
                b.append(j)
        return [a,b]