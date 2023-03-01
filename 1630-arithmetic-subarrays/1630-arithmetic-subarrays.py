class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        val=[]
        for i in range(len(l)):
            res1=(nums[l[i]:r[i]+1])
            res11 = min(res1)
            res2=max(res1)
            check=(res2-res11)//(len(res1)-1)
            x=res11
            while(x<res2):
                if x not in res1:
                    val.append(False)
                    break
                res1.remove(x)    
                x+=check
            if(x==res2):    
                val.append(True)
        return val  