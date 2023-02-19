class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # d=[]
        # for i in nums1:
        #     if i in nums2 and i not in d:
        #         d.append(i)
        # return d
        #i = set(nums1)#the case behind this is that in set repetion is not allowed
        #j = set(nums2)
        return list(set(nums1).intersection(set(nums2)))
        '''the case behind this is that in set repetion is not allowed
     which gives ability for a to find the least not the most                                    repetitve values'''
                        
        '''final= []

        for a in i:
            if a in j:
                final.append(a)
        return final'''
    '''
        return list(set(nums2)-(set(nums2) - set(nums1)))'''
    
        
        