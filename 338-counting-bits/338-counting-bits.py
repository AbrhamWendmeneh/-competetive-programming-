class Solution:
    def countBits(self, n: int) -> List[int]:
        '''        
        val=[]
        for i in range(n+1):
            val.append(i.bit_count())

        return val
        
        '''
        
        val=[]
        for i in range(n+1):
            counter=0
            while i:
                if i & 1:
                    counter +=1
                
                #and by shifting it to the right value of the given                         number
                i >>=1
            val.append(counter)
        return val
                