# 장애물이 없으니까 범위 밖을 나가면 쓰면 됨
# 0,0 에서 시작해서 arr[ci][cj] 에 있는 번호에 맞는 di,dj 로 옮기로
# 만약에 범위 밖을 나가면
# L을 쓸 수 있고, R을 쓸 수 있는데
# 각각 어떤 상태로 도착했는지 visited로 기록해둔다
# 각각 K번까지 사용가능
# 방문했으면 0,0이 됨

# 행 N, 열 M, 주문서 세트의 개수 K
# 상, 우, 하, 좌

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