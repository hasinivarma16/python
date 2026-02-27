arr=[1,2,3,1,1,3]
count=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
            count+=1
print(count)
        
