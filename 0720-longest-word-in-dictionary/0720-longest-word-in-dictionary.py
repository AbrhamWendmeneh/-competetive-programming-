class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        words.sort()
        set_val=set()       
        result=''
        for i in words:
            if len(i) ==1 or (i[:-1] in set_val):
                if len(i) > len(result):
                    result = i
                set_val.add(i)
                    
        return result
                    
        