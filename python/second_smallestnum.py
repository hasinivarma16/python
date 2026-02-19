arr=[3,7,2,9,5]
first_smallest=float('inf')
second_smallest=float('inf')
for i in arr:
    if i<first_smallest:
        second_smallest=first_smallest
        first_smallest=i
    elif i<second_smallest and i!=first_smallest:
        second_smallest=i
print(second_smallest)
