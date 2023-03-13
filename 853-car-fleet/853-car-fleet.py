class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        temp=[]
        
        for i in range(len(position)):
            temp.append((target-position[i],speed[i]))
        temp_val=sorted(temp)
        temp_2=[]
        for j,k in temp_val:    
            val=(j/k)
            '''if temp_2 and val in temp_2 :
                temp_2.pop()'''
            if not temp_2:
                
                temp_2.append(val)
            elif val>temp_2[-1]:
                temp_2.append(val)
        return len(set(temp_2))
            