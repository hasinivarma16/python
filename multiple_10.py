n=int(input())
for _ in range(n):
    x=list(map(int,input().split()))
    if x%10==0:
        print("YES")
    else:
        print("NO")