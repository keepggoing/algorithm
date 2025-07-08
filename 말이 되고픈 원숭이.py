# K번 움직일 수 있다 30 이하
K=int(input())
# 200 이하
M,N=map(int,input().split())
# 0이 평지, 1이 장애물
arr=[list(map(int,input().split())) for _ in range(N)]
v=[[K+1 for _ in range(M)] for _ in range(N)]


from collections import deque

# 몇번 움직임? (시간), 사용한 개수, 좌표
q=deque([(0,0,0,0)])
v[0][0]=0

# 지금 시간은 똑같음
while q:
    time,cnt,ci,cj=q.popleft()

    if (ci,cj) == (N-1,M-1):
        print(time)
        break

    # 그렇다면 말처럼 이동해도 되고 상하좌우 이동해도 되고
    # if cnt<K: 사실 visited에서 걸러져서 없어도 됨

    for di, dj in ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)):
        ni,nj=ci+di,cj+dj
        if 0<=ni<N and 0<=nj<M and arr[ni][nj]==0 and v[ni][nj]>cnt+1:
            q.append((time+1,cnt+1,ni,nj))
            v[ni][nj]=cnt+1

    for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni,nj=ci+di,cj+dj
        if 0<=ni<N and 0<=nj<M and arr[ni][nj]==0 and v[ni][nj]>cnt:
            q.append((time+1,cnt,ni,nj))
            v[ni][nj]=cnt

else:
    print(-1)


