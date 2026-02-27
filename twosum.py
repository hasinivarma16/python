arr=[3,2,4,1,6]
target=5
for i in range(len(arr)):
    for j in range(0,len(arr)):
        if arr[i]+arr[j]==target:
            print(i,j)

        