#Big O(n²)

def Inserction(arr):
    
    for i in range(1, len(arr)):
        
        while arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1],arr[i]
        
    print(arr)
        

