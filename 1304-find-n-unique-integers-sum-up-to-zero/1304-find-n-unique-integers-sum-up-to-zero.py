class Solution:
    def sumZero(self, n: int) -> List[int]:
        val=[]
        if n%2==0:
            
            for i in range(n//2):
                
                val.append(i+1) #the reason i use this is that to exclude 0 in which it starts at 0 form the range of n
                val.append(-i-1)
        else:
            val.append(0)
            for i in range(n//2):
                
                val.append(i+1)
                val.append(-i-1)
        return val