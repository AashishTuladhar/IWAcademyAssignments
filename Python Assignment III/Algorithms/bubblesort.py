def bubbleSort(list): 
    length = len(list) 
  
    for i in range(length): 
        for j in range(0, length-i-1): 
            if list[j] > list[j+1] : 
                list[j], list[j+1] = list[j+1], list[j] 


data = [64, 34, 25, 12, 22, 11, 90] 
  
bubbleSort(data) 
  
print ("Sorted list is:") 
for i in range(len(data)): 
    print (f"{data[i]}",end=" ")