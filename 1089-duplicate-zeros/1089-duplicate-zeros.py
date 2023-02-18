class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # i=0
        # while i <len(arr)-1:
        #     if arr[i]==0:
        #         arr.insert(i+1,0)
        #         i+=2
        #         arr.pop()
        #     else:
        #         i+=1
        a=[]
        for i in arr:
            if i==0:
                a.append(i)
                a.append(0)
                # a+=[0,0]
            else:
                a.append(i)
        # arr=a[0:len(arr)]
        
        for i in range(len(arr)):
            arr[i]=a[i]
                
                
                
                
            
        