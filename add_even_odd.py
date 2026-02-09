arr=[2,7,8,11,3]
even=[]
odd=[]  
sum_even=0
sum_odd=0
for i in arr:
    if i%2==0:
        sum_even+=i
        
    if i%2!=0:
        sum_odd+=i
even.append(sum_even)
odd.append(sum_odd)
print(even+odd)