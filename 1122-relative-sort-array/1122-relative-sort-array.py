class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        a=[]
        for i in arr1:
            if i not in arr2:
                a.append(i)
        a=sorted(a)
        b=[]
        for i in arr2:
            for j in arr1:
                if i ==j:
                    b.append(i)
        return b+a