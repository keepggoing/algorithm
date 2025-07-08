# 모두 녹아서 없어지는 시간
# 모두 녹기 한 시간 전에 남아있는 개수
# 패딩을 준 이유는 사방에 있는 0의 개수를 세라는게 아닐까?
# 문제는 치즈 안에 있는 0
# 신경써야 하는 0은 바깥에 있는 0
# cheese 에서 연결되어있는 부분 모두, 즉 치즈로 연결된 map 내부를 모두 1로 칠하고
# 안에 있는 0을 다른 숫자로 칠해놓으면 좋을 듯
# 회색 입장에서 보면 사방이 다 회색으로 막혀있는거
# 겉에 한줄이 하나씩 없어지는 건데
# 구멍만의 특징이 있을까..?
#
# 결국 겉에 있는 거는 주변에 0이 하나라도 있는 거

# 나 자신은 1, 상하좌우에
# visited가 0이고 arr도 0인 부분이 안에 있는 구멍이 됨
# visited가 0이고 arr이 1인 것 중에서 사방에 visited 1 인게 하나 이상 있는 거가 사라짐
# 그것들은 arr에 0 이 되고 또 이걸 반복한다 !
# 10^4
# bfs란.. 그래프 탐색, 완전 탐색 엣지가 없지 않은 이상 움직일 수 잇음
# 엣지라는 것은 장애물, 끊겨서 더 갈 수 없는 경우
# 이 문제에서 달랐던 건 항상 1인 곳으로 bfs 했는데, 이번엔 0을 기준으로 bfs
N,M=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]

def make_v():
    v = [[0] * M for _ in range(N)]
    v[0][0]=1

    from collections import deque
    q=deque([(0,0)])

    while q:
        ci,cj=q.popleft()
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj=ci+di,cj+dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj]==0 and v[ni][nj]==0:
                v[ni][nj]=1
                q.append((ni,nj))
    return v

v=make_v()
time=0

while sum(map(sum,arr)) != 0:
    cnt=0
    new_arr=[row[:] for row in arr]

    for i in range(N):
        for j in range(M):
            if arr[i][j]==1 and v[i][j]==0 and (v[i-1][j] == 1 or v[i+1][j]==1 or v[i][j+1]==1 or v[i][j-1]==1):
                new_arr[i][j]=0
                cnt+=1
    time+=1
    arr=new_arr
    v=make_v()

print(time)
print(cnt)

# 한번 돌 때 10**4 *3 이게 몇번 ? 10**2 전이니까 괜춘

# ======================

# NxM 모눈종이
# 네변 중에 적어도 두변 이상이 접촉한 것은 사라짐
# 내부 공간은 접촉하지 않음
# 치즈가 모두 녹아 없어지는게 걸리는 시간 구하기
# 치즈 1, 없으면 0
# 치즈가 없는 곳 0에서 시작해서 bfs로 보는데 1이면 녹이고
# 더이상 넣지는 않는다
# visited로 표시해서 2개 이상이면 녹인다

N,M=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]

from collections import deque

for i in range(0, N):
    if arr[i][0] == 0:
        si,sj=i,0
        break

    elif arr[i][M - 1] == 0:
        si,sj=i,M-1
        break
else:
    for j in range(0, M):
        if arr[0][j] == 0:
            si,sj=0,j
            break
        elif arr[N - 1][j] == 0:
            si,sj=N-1,j
            break

time=0
while sum(map(sum,arr)) != 0:
    time+=1
    q=deque([(si,sj)])
    v = [[0] * M for _ in range(N)]
    v[si][sj]=1
    new_arr=[row[:] for row in arr]

    while q:
        ci,cj=q.popleft()
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj=ci+di,cj+dj
            if 0<=ni<N and 0<=nj<M:
                if arr[ni][nj] == 0 and v[ni][nj]==0:
                    q.append((ni,nj))
                    v[ni][nj]=1

                elif arr[ni][nj] == 1 and new_arr[ni][nj] ==1:
                    v[ni][nj]+=1
                    if v[ni][nj]>=2:
                        new_arr[ni][nj]=0
    arr=new_arr

print(time)