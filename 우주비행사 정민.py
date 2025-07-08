# 블랙홀의 개수, 정민이 있는 곳 행,열, 우주선 있는 곳 행,열
K,N1,M1,N2,M2 = map(int,input().split())

# 여기에는 블랙홀 표시
arr1=[[0]*M1 for _ in range(N1)]
arr2=[[0]*M2 for _ in range(N2)]

# 차원 이동 게이트 행,열
A,B = map(int,input().split())

match_gate={}

# 정민이가 있는 곳에서 게이트 좌 상단 내부 좌표
R1,C1 = map(int,input().split())
num=1
for i in range(A):
    for j in range(B):
        match_gate[num]=[(R1+i,C1+j)]
        num+=1

# 우주선이 있는 곳에서 게이트 좌 상단 내부 좌표
num=1
R2,C2 = map(int,input().split())
for i in range(A):
    for j in range(B):
        match_gate[num].append((R2 + i, C2 + j))
        num+=1

match1={}
match2={}

for lst in match_gate.values():
    match1[lst[0]]=lst[1]
    match2[lst[1]]=lst[0]

from collections import deque

q1=deque()
q2=deque()

# 블랙홀
for _ in range(K):
    num,dr,dc=map(int,input().split())
    if num == 1:
        arr1[dr][dc]=1
        q1.append((dr,dc,1))

    else:
        arr2[dr][dc]=1
        q2.append((dr,dc,1))

# ==============================================
def fill_stream(stream,N,M):
    si,sj,sd=0,0,0
    di,dj=dic[for_stream[sd]]

    while True:
        if (si,sj) == (N-1,0):
            stream[si][sj]=4
            break

        ni,nj=si+di,sj+dj

        if 0<=ni<N and 0<=nj<M:
            stream[si][sj]=for_stream[sd]

            if for_stream[sd] == 2:
                sd=(sd+1)%4
                di, dj = dic[for_stream[sd]]

            si,sj=ni,nj

        else:
            sd=(sd+1)%4
            di,dj=dic[for_stream[sd]]

# ==================================================
# 상, 우, 하, 좌, (0,0)으로 순간 이동
dic={0:(-1,0),1:(0,1),2:(1,0),3:(0,-1),4:(0,0)}
for_stream=[1,2,3,2]

stream1=[[0]*M1 for _ in range(N1)]
stream2=[[0]*M2 for _ in range(N2)]

fill_stream(stream1,N1,M1)
fill_stream(stream2,N2,M2)

# ========================================================

# 다 블랙홀로 채워지면 종료
while q1:
    for _ in range(len(q1)):
        ci,cj,time=q1.popleft()
        di,dj=dic[stream1[ci][cj]]
        if (di, dj) == (0, 0):
            ni, nj = 0, 0
        else:
            ni, nj = ci + di, cj + dj

        if arr1[ni][nj]==0:
            arr1[ni][nj]=time+1
            q1.append((ni,nj,time+1))

# 다 블랙홀로 채워지면 종료
while q2:
    for _ in range(len(q2)):
        ci,cj,time=q2.popleft()
        di,dj=dic[stream2[ci][cj]]

        if (di,dj)==(0,0):
            ni,nj=0,0
        else:
            ni,nj=ci+di,cj+dj

        if arr2[ni][nj]==0:
            arr2[ni][nj]=time+1
            q2.append((ni,nj,time+1))

# ===============================================================
# 어쨋든 내가 출발하는 좌표는 1차원의 (0,0) 인 거고, 내가 도착하는 좌표는 2차원의 (N2-1, M2-1)
ans=200*200*200*200*3

def bfs(si,sj,ei,ej):
    global ans
    # 차원, 좌표, 시간
    q=deque([(1,si,sj,1)])
    v1=[[0]*M1 for _ in range(N1)]
    v2=[[0]*M2 for _ in range(N2)]
    v1[si][sj]=1

    while q:
        dim,ci,cj,time=q.popleft()

        if dim==2 and (ci,cj)==(ei,ej):
            ans=min(time-1,ans)

        if dim==1 and 0<=ci<N1 and 0<=cj<M1 and (ci,cj) in match1:
            ni,nj=match1[(ci,cj)]
            if (arr2[ni][nj] == 0 or time + 3 < arr2[ni][nj]) and (v2[ni][nj] == 0 or v2[ni][nj]>time+3):
                q.append((2, ni, nj, time + 3))
                v2[ni][nj] = time+3

        if dim ==2 and 0<=ci<N2 and 0<=cj<M2 and (ci,cj) in match2:
            ni, nj = match2[(ci, cj)] 
            if (arr1[ni][nj] == 0 or time + 3 < arr1[ni][nj]) and (v1[ni][nj] == 0 or v1[ni][nj]>time+3):
                q.append((1, ni, nj, time + 3))
                v1[ni][nj] = time+3

        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj=ci+di,cj+dj
            if dim == 1:
                if 0<=ni<N1 and 0<=nj<M1 and (arr1[ni][nj]==0 or time+1<arr1[ni][nj]) and (v1[ni][nj]==0 or v1[ni][nj]>time+1):
                    q.append((1,ni,nj,time+1))
                    v1[ni][nj]=time+1

            else:
                if 0 <= ni < N2 and 0 <= nj < M2 and (arr2[ni][nj] == 0 or time + 1 < arr2[ni][nj]) and (v2[ni][nj]==0 or v2[ni][nj]>time+1):
                    q.append((2, ni, nj, time + 1))
                    v2[ni][nj]=time+1


bfs(0,0,N2-1,M2-1)

if ans !=200*200*200*200*3:
    print(ans)
else:
    print("hing...")