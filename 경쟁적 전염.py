''' 시간 간당 간당
N,K=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
S,X,Y=map(int,input().split())

from collections import deque

for _ in range(S):
    new_arr=[row[:] for row in arr]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                mn=K+1
                for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                    ni,nj=i+di,j+dj
                    if 0<=ni<N and 0<=nj<N and arr[ni][nj]!=0:
                        mn=min(mn,arr[ni][nj])

                if mn != K+1:
                    new_arr[i][j]=mn
    arr=new_arr

print(arr[X-1][Y-1])

# ================
'''

# NxN 시험관
# 1~K번 바이러스
# 모든 바이러스는 1초마다 네방향 증식
# 낮은 번호를 가진 바이러스부터 먼저 증식하고 이미 누가 있으면 못 들어감
# S초가 지난후 특정 위치의 바이러스 종류 출력
# 존재하지 않으면 0, 1 based index

# 200x200 격자, 1000개 바이러스
# 초별로 끊어서 본다
# q가 여러개인것처럼
# bfs는 순차적으로 실행되기 때문에 쭉 실행해도 상관 없다

N,K=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
S,X,Y=map(int,input().split())

from collections import deque

q=[]
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            q.append((arr[i][j],i,j,0))

q.sort()
q=deque(q)

while q:
    num,ci,cj,time=q.popleft()
    if time==S:
        break
    for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni,nj=ci+di,cj+dj
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0:
            arr[ni][nj]=num
            q.append((ni,nj))

print(arr[X-1][Y-1])





