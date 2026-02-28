arr=[1,2,2,3,1,4,2,3]
dic={}
for i in arr:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1    
print(dic)  #print      