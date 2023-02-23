class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        a=[]
        b=[]
        for i in range(len(nums)):
            
            if i%2!=0:
                a.append(nums[i])
            else:
                b.append(nums[i])
        a=sorted(a)
        a=a[::-1]
        b=sorted(b)
        # c=[]
        val1=0
        val2=0
        for i in range(len(nums)):
            if i%2==0:
                nums[i]=b[val2]
                val2+=1
            else:
                nums[i]=a[val1]
                val1+=1
            # c.append(b[i])
            # c.append(a[i])
        return nums #c