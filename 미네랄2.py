'''
하.. 등호 미친아..
'''
N,M=map(int,input().split())
arr=[list(input()) for _ in range(N)]
K=int(input())
height=list(map(int,input().split()))

for h in range(len(height)):
    # [1] 일단 지우고
    i=N-height[h]       # 내가 찾아야 할 행의 인덱스는 i에 들어감
    if h%2 == 0:        # 왼쪽에서 던지는 거
        for j in range(0,M):
            if arr[i][j]=="x":
                arr[i][j]='.'
                break

    else:               # 오른쪽에서 던지는 거
        for j in range(M-1,-1,-1):
            if arr[i][j]=="x":
                arr[i][j]='.'
                break

    # ================================================
    for row in arr:
        print(*row)
    # [2] bfs 하면서 그룹 찾는다
    # sort해서 기준이 N-1이 아니라면 그 그룹을 당길 수 있는지 찾아보는 거
    from collections import deque

    def bfs(i,j):
        q=deque([(i,j)])
        v[i][j]=1
        lst=[]
        lst.append((i,j))

        while q:
            ci,cj=q.popleft()
            for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                ni,nj=ci+di,cj+dj
                if 0<=ni<N and 0<=nj<M and arr[ni][nj]=='x' and v[ni][nj]==0:
                    q.append((ni,nj))
                    v[ni][nj]=1
                    lst.append((ni,nj))

        lst.sort(key=lambda x:(-x[0],x[1]))
        return lst

    v=[[0]*M for _ in range(N)]
    clusters=[]
    for i in range(N):
        for j in range(M):
            if v[i][j]==0 and arr[i][j]=='x':
                lst=bfs(i,j)
                print(lst)
                clusters.append(lst)
    print(clusters)
    def gravity(cluster):
        global arr

        while True:
            temp=[row[:] for row in arr]
            new_cluster=[]
            for i,j in cluster:
                if 0<=i+1<N and temp[i+1][j]==".":
                    temp[i+1][j]="x"
                    temp[i][j]="."
                    new_cluster.append((i+1,j))
                else:
                    return arr
            arr=temp
            cluster=new_cluster
            cluster.sort(key=lambda x: (-x[0], x[1]))

    clusters.sort(key=lambda x:-x[0][0])
    for cluster in clusters:
        if cluster[0][0] != N-1:
            # 만약 기준점이 맨 마지막이 아니면 하나씩 내릴 준비 !
            new_arr=gravity(cluster)
            arr=new_arr

for row in arr:
    print("".join(row))