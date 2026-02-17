height=[1.73,1.68,1.71,1.89,1.79]
weight=[65.4,59.2,63.6,88.4,68.7]
bmi=[]
for i in range(len(height)):
    bmi.append(weight[i]/(height[i]**2))
print(bmi)