class Solution:
    def minSteps(self, n: int) -> int:
        val=0
        init=2 
        while init**2 <=n:
            while n%init==0:
                val+=init
                n//=init
            init+=1
        if n!=1:
            val+= n
        return val