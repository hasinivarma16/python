#Upper bound of target element
arr=[2,3,6,7,8,8,11,11,11,12]
target=9
low=0
high=len(arr)-1
result=len(arr)
while low<=high:
    mid=(low+high)//2
    if arr[mid]>target:
        result=mid
        high=mid-1
    else:
        low=mid+1
if result == len(arr):
    print("Element not found. Length of array is:", len(arr))
else:
    print("Smallest index of target element is:", result)