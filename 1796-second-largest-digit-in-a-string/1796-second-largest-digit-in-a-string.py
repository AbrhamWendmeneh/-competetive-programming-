class Solution:
    def secondHighest(self, s: str) -> int:
        
        a=[]
        check_set=set()
        for i in s:
            if i.isdigit():
                if i not in check_set:
                    check_set.add(i)
                    a.append(int(i))
        if len(check_set)<2:
            return -1
        
        return sorted(a)[-2]
        