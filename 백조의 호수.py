# N,M=map(int,input().split())
# # . 물, X 빙판, L 백조
# arr=[list(input()) for _ in range(N)]
#
# # Q 백조가 있는 공간은? -> 일단 가능하다고 생각
# # 빙판에 백조가 있진 않을 거니까..
#
# from collections import deque
# q=deque()
# v=[[float('inf')]*M for _ in range(N)]
#
# # 백조의 위치 찾기 10^4
# loc=[]
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == "L":
#             loc.append((i,j))
#         if arr[i][j] != 'X':
#             # 빙하가 아니면 항상 갈 수 있음
#             v[i][j]=0
#             for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
#                 ni,nj=i+di,j+dj
#                 if 0<=ni<N and 0<=nj<M and arr[ni][nj]=='X':
#                     q.append((i,j))
#                     break
# # 10^4
# day=0
# while q:
#     # day에 녹는 좌표
#     for _ in range(len(q)):
#         ci,cj=q.popleft()
#         for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
#             ni,nj=ci+di,cj+dj
#             if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 'X' and v[ni][nj]>day+1:
#                 q.append((ni,nj))
#                 v[ni][nj]=day+1
#     day+=1
#
# si,sj=loc[0]
# ei,ej=loc[1]
#
# # 멀리가도 괜찮으니 숫자가 작은 곳만 밟아서 가기
# # 여기까지 오는데 사용된 숫자 중 가장 작은 거 더 크면 안 와도 됨
# # 최단 거리가 아니라 적혀있는 숫자가 가장 적은
# # 모든 경로를 본다?
# # 밟을 수 있는지 없는지?
#
# from heapq import *
# v2=[[float('inf')]*M for _ in range(N)]
# hq=[(0,si,sj)]
# v2[si][sj]=0
#
# while hq:
#     time,ci,cj = heappop(hq)
#     if (ci,cj) == (ei,ej):
#         print(time)
#         break
#
#     for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
#         ni,nj=ci+di,cj+dj
#
#         if 0<=ni<N and 0<=nj<M and v2[ni][nj]>max(v[ni][nj],time):
#             heappush(hq,(max(v[ni][nj],time),ni,nj))
#             v2[ni][nj]=max(v[ni][nj],time)

# 견우와 직녀 기다리는 거 계속 큐에 넣으면서
# logN N은 힙에 들어있는 개수, pop push 할 때마다 이 정도
# 힙을 안 쓰는 다른 방법..
# 먼저 녹이지 말고
# 출력
# 걸리는 날
# 걸리는 날을 기준으로 heapq로 빼고 도착하자마자?


# 불처럼 큐 두개!!!
# N 개가 정해져있는데, N개를 오름차순으로 하고 싶으면
# 걍 정렬하면 되지 N이 가변적인 숫자가 아니니까
# 힙은 관리하기 편하지만 오버헤드
# N개가 가변적일 때 힙큐가 낫지, 게속 넣고 정렬하면 NlogN x N 번 정도니까


from collections import deque

N,M=map(int,input().split())
arr=[list(input()) for _ in range(N)]

loc=[]
melt=deque()
vs=[[0]*M for _ in range(N)]
vm=[[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == "L":
            loc.append((i,j))
        elif arr[i][j] != "X":
            for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
                ni,nj=i+di,j+dj
                if 0<=ni<N and 0<=nj<M and arr[ni][nj]=='X':
                    melt.append((i, j))
                    vm[i][j] = 1
                    break

si,sj=loc[0]
ei,ej=loc[1]
swan=deque([(si,sj)])
vs[si][sj]=1


def solve():
    day=0
    while True:
        # 백조는 갈 수 있을 때까지 간다
        # 이걸 기록해두고 !
        temp=[]
        while swan:
            ci,cj=swan.popleft()

            if (ci,cj) == (ei,ej):
                return day

            for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                ni,nj=ci+di,cj+dj
                if 0<=ni<N and 0<=nj<M and vs[ni][nj]==0:
                    if arr[ni][nj] != 'X':
                        swan.append((ni,nj))
                        vs[ni][nj]=1
                    else:
                        temp.append((ni,nj))
                        vs[ni][nj]=1
                        # 큐에 들어갈 때 하는 행동은 무조건 똑같음
                        # 이게 아무리 temp 여도 나중에 swan 큐가 될 거자나

        swan=deque(temp)

        for _ in range(len(melt)):
            ci,cj=melt.popleft()
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni, nj = ci + di, cj + dj
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 'X' and vm[ni][nj] == 0:
                    arr[ni][nj]='.'
                    melt.append((ni,nj))
                    vm[ni][nj]=1
        day+=1

print(solve())

# bfs 메모리 초과 시간 초과는 q에 너무 많이 넣은 거 무조건
# visited 관리 물애서는 필요없음
# 이런거 반례 생각할 때 한줄 생각해보기 !!!!
# 백조만 물인 예시
