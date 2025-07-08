N=int(input())
arr=[[0]*102 for _ in range(102)]

for _ in range(N):
    y,x=map(int,input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            arr[i][j]=1

arr_t=list(map(list,zip(*arr)))
ans=0
# 0/1 이어 나오면 바뀌는 거 -> 다 더하면 둘레
for lst in arr:
    for i in range(101):
        if lst[i]+lst[i+1]==1:
            ans+=1

for lst in arr_t:
    for i in range(101):
        if lst[i]+lst[i+1]==1:
            ans+=1
print(ans)