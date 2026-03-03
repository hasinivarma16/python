arr=[3,5,8,15,19]
target=18
ans=len(arr)
left=0
right=len(arr)-1

while left<=right:
    mid=(left+right)//2   #becoz for every loop mid changes/updates
    if arr[mid]>=target:
        ans=mid
        right=mid-1
    else:
        left=mid+1
print(ans)