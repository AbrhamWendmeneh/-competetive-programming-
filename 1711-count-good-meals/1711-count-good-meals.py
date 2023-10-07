class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        store={}
        count=0
        power2list=[1]
        for j in range(21):
            power2list.append(power2list[-1]*2)
        for i in deliciousness:
            for pw2 in power2list:
                if pw2 -i in store:
                    count+=store[pw2 - i]
                
            store[i]=store.get(i,0)+1
    
        return count %((10**9)+7)
                
                
        