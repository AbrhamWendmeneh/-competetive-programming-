class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        i=2
        prime=[True] * n
        prime[0]=False
        prime[1]=False        
        while i**2 < n:
            if prime[i]:               
                for j in range(i*i, n, i):
                    prime[j]=False
            i+=1
          
        return sum(prime)

