class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
     
        a = []
        for i in nums1:
            b = nums2.index(i)
            # if :
            c=len(nums2)
            while b < c:
                if b<c-1 and nums2[b+1] > i:
                    a.append(nums2[b+1])
                    break
                b+=1
            else:
                a.append(-1)
        return a
            
