class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        '''for i in range(len(names)):
            for j in range(i+1,len(names)):
                if heights[i]>heights[j]:
                    heights[i],heights[j]=heights[j],heights[i]
                    names[i],names[j]=names[j],names[i]
        return names'''
        a=[]
        for i in range(len(names)):
            a.append((heights[i],names[i]))
        # a.sort()
        # b=[]
        # for j in a:
        #     b.append(j)[1]
        # return b
        
        a=sorted(a,reverse=True)
        b=[]
        for j in range(len(a)):
            b.append(a[j][1])
        return b
        