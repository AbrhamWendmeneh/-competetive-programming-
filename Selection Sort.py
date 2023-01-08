class Solution: 
    def select(self, arr, i):
        # code here 
        return
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            t=i
            for j in range(i,n):
                if arr[j]<arr[t]:
                    t=j
            arr[i],arr[t]=arr[t],arr[i]
            
        return arr
