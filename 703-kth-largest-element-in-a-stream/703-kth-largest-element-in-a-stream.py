class KthLargest:

    def __init__(self, k: int, nums: List[int]):
       
        self.minheap=nums
        self.value=k
        #this is to make the element to be sorted in the case of min heap order 
        # and all of the elements are sorted 
        heapq.heapify(self.minheap)
        
        #this is the case so as to make simplify getting the values which are in the range of k 
        # for instance in this case [3, [4, 5, 8, 2]] the value which are not useful for are being ignored like 2 and values which are less than it
        
        while len(self.minheap) > k:
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap,val)
        if len(self.minheap) > self.value:
            heapq.heappop(self.minheap)
        return self.minheap[0]
            

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)