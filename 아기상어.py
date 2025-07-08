'''
- 리팩토링한 코드
단계별, 즉 거리별로 끊어서 bfs를 돌리는 거 ! 준영프로님께 배웠다
아직 어색하니 연습 또 연습 !

로직 정리 & 필요 없는 코드 정리
[1] 현재 사이즈와 비교해서 물고기 크기가 더 작고 & 갈 경로도 있는 곳을 poss에 넣어준다
[2] poss에 넣을 때 (거리, 좌표)로 넣어주고, 거리가 짧고 - i가 작고 - j가 작은 순대로 정렬한다
** 여기서 다 넣어줄 필요 없이 갈 수 있는게 나왔다면 그 동일한 거리까지만 돌려주면 됨
머리로는 생각했는데 어떻게 구현할지 몰랐음 -> 이계 단계별 bfs의 활용점 **
[3] 가장 앞에 있는 곳으로 이동하고, 현재 위치도 바꿔주고, 거리만큼 time에 더해준다
[4] 현재 위치가 바꼈으니 다시 시작한다

'''

# 제출한 코드 1072ms
from collections import deque

def can_go(si,sj,x,y):
    global size
    # 이건 어떻게 해서든 si,sj 에서 x,y로 가면 됨
    q=deque([(si,sj)])
    v=[[0]*N for _ in range(N)]
    v[si][sj]=1

    while q:
        ci,cj=q.popleft()
        if ci==x and cj==y:
            return v[ci][cj]-1

        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj=ci+di,cj+dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj]<=size and v[ni][nj]==0:
                q.append((ni,nj))
                v[ni][nj]=v[ci][cj]+1
    return -1

N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
size=2
poss=[]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            si,sj=i,j
            arr[i][j] = 0

for i in range(N):
    for j in range(N):
        if 0<arr[i][j]<size:
            dis=can_go(si,sj,i,j)
            if dis != -1:
                poss.append((dis,i,j))
time=0
plus=0

while True:
    poss = sorted(poss, key=lambda x: (x[0], x[1], x[2]))
    # 갈 수 있는 곳이 있다면
    if poss:
        d,x,y=poss[0]
        # 먹었으니 0으로 바꾸고
        arr[x][y]=0
        # 좌표 옮기고
        si,sj=x,y
        plus+=1

        if plus==size:
            size+=1
            plus=0

        time+=d
    # 갈 수 있는 곳이 없다면 멈춘다
    else:
        print(time)
        break

    # 돌고 나서 poss에 다시 넣는다
    poss=[]
    for i in range(N):
        for j in range(N):
            if 0 < arr[i][j] < size:
                dis = can_go(si, sj, i, j)
                if dis != -1:
                    poss.append((dis, i, j))


''' 리팩토링한 코드 124ms
from collections import deque

N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]

# 일단 상어 위치 찾아 !
found=False
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            si,sj=i,j
            arr[si][sj]=0
            found=True
    if found:
        break

# 이건 시간
time=0
size=2
plus=0

while True:
    # 이거는 돌아올 때마다 초기화 되어야 하니까 여기서 해야하구
    v = [[0] * N for _ in range(N)]
    q = deque([(si, sj)])
    v[si][sj] = 1
    # 요거는 갈 수 있는 최단거리 좌표들을 담는 거구
    # 여기에 뭔가 있으면 이제 bfs 멈춰도 되는 거구
    lst=[]
    # 거리가 1일때 보고, 2일때 보고, 3일때 보고
    # 이렇게 끊어서 볼 거니까 q에 길이만큼만 반복해서 볼거야
    # 여기가 그냥 if이면 안 되는 이유는 하나만 보는게 아니라 다음 것도 봐야하니까?
    while q:
        for _ in range(len(q)):
            ci, cj=q.popleft()
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni, nj = ci + di, cj + dj
                # 작고, 같고, 아무것도 없는 거 모두 만족하니까
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] <= size and v[ni][nj] == 0:
                    q.append((ni, nj))
                    v[ni][nj]=v[ci][cj]+1

                    if 0 < arr[ni][nj] < size:
                        lst.append((ni, nj))

        # 이만큼 다 돌았는데 lst가 있으면
        if lst:
            lst.sort()
            x,y=lst[0]
            arr[x][y]=0
            si,sj=x,y
            plus+=1
            found=True

            if size==plus:
                size+=1
                plus=0
            # 이걸 더하는 이유는 v에 적혀있는거 -1이 거리가 될 테니까
            # 이게 좀 의심..?
            time += v[si][sj]-1
            break
        # 만약에 바꼈으면 하나 더 나가서 새로운 위치에서 si,sj 해야하니까 나가야함

    # q에 더이상 아무것도 없으면 갈 곳이 없는 거니까
    else:
        print(time)
        break

'''