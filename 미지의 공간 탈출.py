# N은 미지의 공간 한 변의 길이, M은 시간의 벽 한 변의 길이, F는 시간 이상 현상의 개수
N,M,F=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
ipt=[[list(map(int,input().split())) for _ in range(M)] for _ in range(5)]        # 0: 동 // 1: 서 // 2: 남 (앞) // 3: 북 (뒤) // 4: 윗면

ipt[0]=list(map(list,zip(*ipt[0])))[::-1]                                         # 동쪽 평면도는 반시계방향 회전
ipt[1]=list(map(list,zip(*ipt[1][::-1])))                                         # 서쪽 평면도는 시계방향 회전
ipt[3]=[row[::-1] for row in ipt[3][::-1]]                                        # 북쪽 평면도는 행도, 열도 뒤집어

ball=[]                                                                           # 3차원을 2차원으로 뭉개기
for i in range(M):
    ball.append([0]*M+ipt[3][i]+[0]*M)
    ball.append(ipt[1][i]+ipt[4][i]+ipt[0][i])
    ball.append([0]*M+ipt[2][i]+[0]*M)

# ====================================================================================
ch={}                                                                             # ch 딕셔너리에는 평면도에서 연결 안 되는 부분을 연결시킴

for i in range(M):
    # 좌상단
    ch[(M,i)]=(i,M)
    ch[(i,M)]=(M,i)

    # 우상단
    ch[(i,2*M-1)]=(M,3*M-(i+1))
    ch[(M,3*M-(i+1))]=(i,2*M-1)

    # 좌하단
    ch[(2*M-1,i)]=(3*M-(i+1),M)
    ch[(3*M-(i+1),M)]=(2*M-1,i)

    # 우하단
    ch[(2*M+i,2*M-1)]=(2*M-1,2*M+i)
    ch[(2*M-1,2*M+i)]=(2*M+i,2*M-1)


# ====================================================================================

for i in range(3*M):
    for j in range(3*M):
        if ball[i][j] == 2:                           # ball에서 시작점은 b_si,b_sj
            b_si,b_sj=i,j

# ====================================================================================
# 우, 하, 좌, 상 순서
dic={0:(0,1),1:(1,0),2:(0,-1),3:(-1,0)}

flag=False
for i in range(N):
    for j in range(N):
        if arr[i][j] == 3:                            # arr에서 출구 위치 찾을 건데
            si,sj=i,j                                 # 일단 시간의 벽을 나타내는 3이 제일 먼저 나오는 인덱스를 찾고
            flag=True
            break
    if flag:
        break

si,sj=si-1,sj-1                                       # 위로 한칸, 왼쪽으로 한칸 간 다음에 달팽이처럼 움직일거임
sd=0

def exit(si,sj,sd):
    while True:
        for i in range(M+1):
            di,dj=dic[sd]
            si,sj=si+di,sj+dj
            # 0이고 모서리가 아니면
            if arr[si][sj]==0 and i !=M:
                return i,si,sj,sd
        sd+=1

idx,ei,ej,ed=exit(si,sj,sd)

if ed == 0:     # 우
    b_ei,b_ej=0,M+idx
elif ed == 1:   # 하
    b_ei,b_ej=M+idx,3*M-1
elif ed == 2:   # 좌
    b_ei,b_ej=3*M-1,3*M-1-M-idx
elif ed == 3:   # 상
    b_ei,b_ej=3*M-1-M-idx,0

from collections import deque

def bfs(b_si,b_sj,b_ei,b_ej):
    q=deque([(b_si,b_sj,0)])
    v=[[0]*(3*M) for _ in range(3*M)]
    v[b_si][b_sj]=1
    while q:
        ci,cj,time=q.popleft()
        if (ci,cj) == (b_ei,b_ej):
            return time
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj=ci+di,cj+dj
            if 0<=ni<3*M and 0<=nj<3*M:
                if (ni,nj) in ch:
                    if (ni,nj)==(M-1,M-1) or (ni,nj)==(M-1,2*M) or (ni,nj)==(2*M,M-1) or (ni,nj)==(2*M,2*M):
                        for nni,nnj in ch[(ni,nj)]:
                            if (nni,nnj) != (ci,cj):
                                ni,nj=nni,nnj
                    else:
                        ni,nj=ch[(ni,nj)][0]
                if ball[ni][nj] == 0 and v[ni][nj] == 0:
                    q.append((ni,nj,time+1))
                    v[ni][nj]=1
    return -1

if ball[b_ei][b_ej]==1:
    print(-1)
else:
    time=bfs(b_si,b_sj,b_ei,b_ej)

    if time == -1:
        print(-1)
    else:
        # ========================================
        # 시간 이상 현상을 위한 dic
        # 동,서, 남,북
        si,sj=ei,ej         # 출구 위치
        for i in range(N):
            for j in range(N):
                if arr[i][j]==4:
                    ei,ej=i,j

        t_dic={0:(0,1),1:(0,-1),2:(1,0),3:(-1,0)}
        strange=[]
        for _ in range(F):
            r,c,d,v=map(int,input().split())
            strange.append((r,c,d,v))
            arr[r][c]=1

        for turn in range(1,time+1):
            for k in range(len(strange)):
                if strange[k]!=-1:
                    r,c,d,v=strange[k]
                    if turn % v == 0:
                        di,dj=t_dic[d]
                        ni,nj=r+di,c+dj
                        if 0<=ni<N and 0<=nj<N and arr[ni][nj]==0:
                            arr[ni][nj]=1
                            strange[k]=[ni,nj,d,v]
                        else:
                            strange[k]=-1
        # ======================================================= 출구에 왔을 때까지의 일
        def bfs2(si,sj,ei,ej):
            global time
            time+=1

            # 9초 처리 먼저하고
            for k in range(len(strange)):
                if strange[k]!=-1:
                    r,c,d,v=strange[k]
                    if time % v == 0:
                        di,dj=t_dic[d]
                        ni,nj=r+di,c+dj
                        if 0<=ni<N and 0<=nj<N and arr[ni][nj]==0:
                            arr[ni][nj]=1
                            strange[k]=[ni,nj,d,v]
                        else:
                            strange[k]=-1
            # 출구가 벌써 막히면
            if arr[si][sj]==1:
                return -1   # -1 return 하고
            else:       # 출구 안 막히면 bfs 시작
                q = deque([(si, sj, time)])
                visited = [[0]*N for _ in range(N)]
                visited[si][sj]=1

                while q:
                    for k in range(len(strange)):
                        if strange[k] != -1:
                            r, c, d, v = strange[k]
                            if (time+1) % v == 0:
                                di, dj = t_dic[d]
                                ni, nj = r + di, c + dj
                                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
                                    arr[ni][nj] = 1
                                    strange[k] = [ni, nj, d, v]
                                else:
                                    strange[k] = -1
                    time += 1

                    for _ in range(len(q)):
                        ci, cj, t = q.popleft()
                        if (ci, cj) == (ei,ej):
                            return t
                        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                            ni, nj = ci + di, cj + dj
                            if 0<=ni<N and 0<=nj<N and arr[ni][nj]!=1 and visited[ni][nj]==0:
                                q.append((ni,nj,t+1))
                                visited[ni][nj]=1
                return -1
        ans=bfs2(si,sj,ei,ej)

        print(ans)

