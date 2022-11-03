class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        newnums=sorted(nums)		
        val=[-1]*len(nums)		
        middle_index=len(nums)//2
        middle_num=newnums[middle_index]
		
        for i in range(1,len(nums),2):			
            if newnums[0] < middle_num:
				item=newnums.pop(0)
				val[i]=item
		
        for i in range(0,len(nums),2):
			if len(newnums):
				item=newnums.pop(0)

				val[i]=item
		
        return val
        
















