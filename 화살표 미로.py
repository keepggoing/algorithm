'''
left와 right를 합쳐서 관리했을 때 안 되나?
-> 안될 듯 같은 곳에 왼쪽 남겨서 오고
같은 곳에 와도 오른쪽 한 쪽 남은 거랑 왼쪽 한쪽 남은 거랑 다르자나
'''
dic={0:(-1,0),1:(0,1),2:(1,0),3:(-1,0)}

N,M,K=map(int,input().split())
arr=[list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == "U":
            arr[i][j]=0

        elif arr[i][j] == "D":
            arr[i][j]=2

        elif arr[i][j] == "L":
            arr[i][j]=3
        else:
            arr[i][j]=1

from collections import deque
# 좌표, left, right
q=deque([(0,0,0,0)])
v=[[[K+1,K+1] for _ in range(M)] for _ in range(N)]
for row in v:
    print(*row)

while q:
    ci,cj,left,right=q.popleft()
    if (ci,cj) == (N-1,M-1):
        print("Yes")
        break

    d=arr[ci][cj]
    di,dj=dic[d]
    ni,nj=ci+di,cj+dj

    # 총 개수가 더 크거나, 같다면 형태가 다르거나
    if 0<=ni<N and 0<=nj<M and (sum(v[ni][nj])>left+right) or (sum(v[ni][nj])==left+right and (v[ni][nj][0], v[ni][nj][1]) != (left, right)):
        q.append((ni,nj,left,right))
        v[ni][nj]=[left,right]

    # ====
    d=(arr[ci][cj]-1)%4
    di,dj=dic[d]
    ni,nj=ci+di,cj+dj
    if 0<=ni<N and 0<=nj<M and (sum(v[ni][nj])>left+right+1) or (sum(v[ni][nj])==left+right+1 and (v[ni][nj][0], v[ni][nj][1]) != (left+1, right)):
        q.append((ni,nj,left+1,right))
        v[ni][nj]=[left+1,right]

    # ====
    d = (arr[ci][cj]+1)%4
    di, dj = dic[d]
    ni, nj = ci + di, cj + dj
    if 0 <= ni < N and 0 <= nj < M and (sum(v[ni][nj])>left+right+1) or (sum(v[ni][nj])==left+right+1 and (v[ni][nj][0], v[ni][nj][1]) != (left, right+1)):
        q.append((ni, nj, left, right+1))
        v[ni][nj] = [left, right+1]

else:
    print("No")
