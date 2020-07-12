def binarySearch(list, start, stop, item):
    while start <= stop:
        mid = start + (stop - start)
        if list[mid] == item:                     
            return mid
        elif list[mid] < item:                   
            start = mid + 1
        else:                                     
            stop = mid - 1
    return -1                                     

numbers = [0,99,2,6,4,8,12,13,17,15]
print("Sorted numbers",sorted(numbers))
item = 13
  
result = binarySearch(sorted(numbers), 0, len(numbers)-1, item) 
  
if result != -1: 
    print("Element is present at index % d" %result) 
else: 
    print("Element is not present in list") 