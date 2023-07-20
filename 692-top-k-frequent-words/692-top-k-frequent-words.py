class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dict_val={}
        for i in words:
            if i in dict_val:
                dict_val[i]+=1
            else:
                dict_val[i]=1
        sorted_words =sorted(dict_val.keys(),key=lambda word: (-dict_val[word], word))
        return sorted_words[:k]
    
    