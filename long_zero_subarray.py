arr=[9,-3,3,-1,6,-5]
sum=0
count=0
max_len=0
for i in range(len(arr)):
    total=0
    for j in range(i,len(arr)):
        total+=arr[j]
        if total==sum:
            length=j-i+1
            if length>max_len:
                max_len=length
            for x in range(i,j+1):
                print(arr[x],end=" ")
            print()
print("max_length",max_len)            

