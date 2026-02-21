arr=[3,7,2,9,5]
first_lar=float('-inf')
second_lar=float('-inf')
for i in arr:
    if i>first_lar:
        second_lar=first_lar
        first_lar=i
    elif i>second_lar and i!=first_lar:
        second_lar=i
print(second_lar)
