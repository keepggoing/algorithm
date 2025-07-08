# 14:15~
# NxN 게임판, 8방향 (7방향), 빈칸 . , 벽 #, 목적지 F
# 빈 공간 중 어느 지점에 캐릭터 두고 시작
# 목적지에 도달할 수 있도록 하는 시작 지점의 개수 구하기
# 2000
# 목적지에서 시작해서 갈 수 있는 방향대로 가보고
# . 이면 cnt+=1, visited 처리하구

N=int(input())
arr=[list(input()) for _ in range(N)]
v=[[0]*N for _ in range(N)]
# 아래로 이동하는게 안됨

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'F':
            si,sj=i,j

from collections import deque
q=deque([(si,sj)])
cnt=0

while q:
    ci,cj=q.popleft()
    for di,dj in ((-1,0),(0,-1),(0,1),(1,1),(1,-1),(-1,1),(-1,-1)):
        ni,nj=ci+di,cj+dj
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] == "." and v[ni][nj]==0:
            cnt+=1
            q.append((ni,nj))
            v[ni][nj]=1

print(cnt)