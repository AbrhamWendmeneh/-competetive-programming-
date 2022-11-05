def countSwaps(a):
    # Write your code here
    sorted = False
    swaps = 0
    
    while not sorted:
        sorted = True
        
        for i in range(len(a)-1):
            if a[i] > a[i +1]:
                a[i], a[i+1] = a[i+1], a[i]
                swaps +=1
                sorted = False
    
    print("Array is sorted in",swaps, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[len(a)-1])
    return a
