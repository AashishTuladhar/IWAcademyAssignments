def interpolationSearch(list, n, x):  
    low = 0
    high = (n - 1) 
   
    while(low <= high and x >= list[low] and x <= list[high]): 
        if low == high: 
            if list[low] == x:  
                return low 
            return -1
          
        pos  = low + int(((float(high - low) / 
            ( list[high] - list[low])) * ( x - list[low]))) 
  
        if list[pos] == x: 
            return pos 
   
        if list[pos] < x: 
            low = pos + 1
   
        else: 
            high = pos - 1
      
    return -1
  

data = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47] 
n = len(data) 
  
print("Sorted list is:", sorted(data))
x = 18 
index = interpolationSearch(data, n, x) 
  
if index != -1: 
    print("Element found at index",index)
else: 
    print("Element not found")