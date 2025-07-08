# N개의 서로 다른 운동 키트, 하루 지날 때마다 K만큼 감소
N,K=map(int,input().split())

# 운동 키트 증가량
lst=list(map(int,input().split()))


# [1] 운동 키트의 순서를 정하는 순열
# n은 지금까지 몇개 정했냐, 하나 정할 때마다 500이상인지 확인해야함
def dfs(n):
    global ans
    if n==N:
        ans+=1
        return

    for i in range(N):
        # 여기서 그때 그때 500이상인지 확인
        if lst[i]-K>=0 and v[i]==0:
            v[i]=1
            dfs(n+1)
            v[i]=0


# 정답이 되는 경우의 수
ans=0
v=[0]*N
dfs(0)

print(ans)
