class Solution:
    # import math
    def sumSubarrayMins(self, arr: List[int]) -> int:
        '''        ans=0
        right=1
        while True:
            if right<len(arr):
                ans+=min(arr[left:right])'''
        # temp=[]
        # b=0
        # for i in range(len(arr)):
        #     for j in range(i,len(arr)):
        #         b+=min(arr[i:j+1])
        # return b%((10**9)+7)
        # arr=arr.append(-math.inf)+[-math.inf]
        temp=[-math.inf]+arr+[-math.inf]
        n=0
        result=0
        array_val=[]
        while n< len(temp):
            
            while array_val and temp[array_val[-1]]> temp[n]:
                mid_val=array_val.pop()
                left_val=array_val[-1]
                right_val=n
                result+=temp[mid_val]*(mid_val-left_val)*(right_val-mid_val)
            array_val.append(n)
            n+=1
        return result%((10**9)+7)
            