num=[1,1,2,2,3]
i=0
j=i+1
for i in range(len(num)-1):
    for j in range(i+1,len(num)-1):
        if num[i]==num[j]:
            num.remove(j)
print(num)