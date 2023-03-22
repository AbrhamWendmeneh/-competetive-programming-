class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        '''
        if len(s1)>len(s2):
            return False
        low=0
        high=len(s1)
        while low<(len(s2)-len(s1)+1):
            if sorted(s2[low:low+high])==sorted(s1):
                # print(high)  
                return True
            else:
                low+=1
                
                # print(high)
        return False'''
        
        if len(s1)>len(s2):
            return False
        s1_count=Counter(s1) 
        counter=Counter()
        for i,j in enumerate(s2):
            counter[j]+=1
            # print(counter)
            if i>=len(s1):
                left=s2[i-len(s1)]
                # print(left)
                if counter[left]==1:
                    del counter[left]
                else:
                    # print(counter[left])
                    counter[left]-=1
            if counter==s1_count:
                return True
        return False
        
        