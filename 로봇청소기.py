while True:
    M,N=map(int,input().split())
    if (N,M) == (0,0):
        break

    arr=[list(input()) for _ in range(N)]
    dirty=[]
    m={}
    idx=0

    for i in range(N):
        for j in range(M):
            if arr[i][j] == "*":
                dirty.append((i,j))
                m[(i,j)]=idx
                idx+=1

            elif arr[i][j] == "o":
                si,sj=i,j

    # ===============================

    from collections import deque
    
    def check(si,sj,ei,ej):
        v=[[0]*M for _ in range(N)]
        q=deque([(si,sj)])
        v[si][sj]=1

        while q:
            ci,cj=q.popleft()
            if (ci,cj) == (ei,ej):
                return v[ci][cj]-1

            for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                ni,nj=ci+di,cj+dj
                if 0<=ni<N and 0<=nj<M and arr[ni][nj] != "x" and v[ni][nj]==0:
                    q.append((ni,nj))
                    v[ni][nj]=v[ci][cj]+1
        return -1

    # =================================

    CNT=len(dirty)
    match=[[0]*CNT for _ in range(CNT)]
    init=[0]*CNT

    for i in range(CNT):
        init[i]=check(si,sj,dirty[i][0],dirty[i][1])
        for j in range(i+1,CNT):
            match[i][j]=check(dirty[i][0],dirty[i][1],dirty[j][0],dirty[j][1])
            match[j][i]=match[i][j]

    mn=float('inf')
    # 백트래킹 안에 bfs를 넣으면
    # 몇번 도달 x N x M
    # ================================

    def btk(cnt, new):
        global mn

        if cnt == len(dirty):
            total=0
            if init[m[new[0]]] != -1:
                total+=init[m[new[0]]]
                for i in range(len(new)-1):
                    if match[m[new[i]]][m[new[i+1]]] != -1:
                        total+=match[m[new[i]]][m[new[i+1]]]
                        if total>=mn:               # 가지치기
                            return
                    else:
                        return
                mn=min(mn,total)
            return

        for i in range(len(dirty)):
            # 인덱스가 들어가는 것
            if v[i] == 0:
                # 내가 가지치기 하고 싶은 것은 아예 순열을 안 만들어도 되는 거
                if new and match[m[new[-1]]][i]!=-1:
                    v[i] = 1
                    new.append(dirty[i])
                    btk(cnt + 1, new)
                    new.pop()
                    v[i] = 0

    v = [0] * len(dirty)
    btk(0, [])
    if mn == float('inf'):
        print(-1)
    else:
        print(mn)

