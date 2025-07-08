N,M=map(int,input().split())

adj=[[] for _ in range(N+1)]
lst=[0]*(N+1)
ans=[0]*(N+1)

for _ in range(M):
    a,b=map(int,input().split())
    adj[a].append(b)
    lst[b]+=1

from collections import deque
q=deque()

for i in range(1,N+1):
    if lst[i]==0:
        q.append(i)
        ans[i]=1


# for n in adj[c]: 이게 고정된게 아니자나
# E번 보는 거지 (간선의 수)
# 고정되면 인접행렬이면 노드만큼 N**2
# 만약 인접리스트가 무향이다? 많이 들어가서 N**2정도라고 생각하면 됨

while q:
    c=q.popleft()
    for n in adj[c]:
        lst[n]-=1
        if lst[n]==0:
            q.append(n)
            ans[n]=ans[c]+1

print(*ans[1:])
