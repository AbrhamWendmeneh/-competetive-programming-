class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # for i in range(len(s)):
        #     for j in range(2):
        array=[0]*(len(s)+1)
        for i,j,k in shifts:
            
            #for the forward shift
            if k==1:
                array[i]+=1
                array[j+1]-=1
            else:
                array[i]-=1
                array[j+1]+=1
        #prefix sum
        for n in range(1,len(s)):
            array[n]+=array[n-1]
        result=[]
        for i ,j in enumerate(s):
            cur=(ord(j)-ord('a')+array[i])%26
            result.append(chr(cur+ord('a')))
        return ''.join(result)
        
                
                