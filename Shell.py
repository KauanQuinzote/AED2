#Big O inconstante, no pior caso geralmente O(n²)

import Inserction

def Shell(arr):
    
    gap = int(len(arr)/2)
    
    while gap > 0:
        i = 0
        
        while i+gap < len(arr):
            
            if arr[i+gap] < arr[i]:
                arr[i], arr[i+gap] = arr[i+gap], arr[i]
            i+=1
        gap = int(gap/2)
    print(arr)
    Inserction.Inserction(arr)
    
    

arr = [0, 5, 8, 4, 7, 9, 12, 11, 8, 2, 1, 20, 6, 3]

Shell(arr)
