
arr=[2,3,4,7,8,9]
len_arr=len(arr)
if len_arr%2==0:
    median=(arr[len_arr//2]+arr[(len_arr//2)-1])/2 #divide
else:
    median=arr[len_arr//2]#print median
print(median)