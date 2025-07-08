''' 2차 풀이
[0] 타임라인
구상 (35분)
구현 (30분)
디버깅 (30분)

[1] 실수한 점
1. 하드코딩 잘못 옮겨적음
2. bfs에서 amount == 1 됐을 때 중단하는 코드 빠짐
bfs에서 큐에 좌표 외 다른 값도 같이 넣고, 그 값이 종료조건이 될 때 자주 누락함 **

-> 둘다 자주 하는 실수, 체크리스트 추가하기

[2] 배울점
1. " 두 좌표의 대소 비교 후 큰 값에서 차이만큼 빼고, 작은 값에서 차이만큼 더하고 " 이 부분 구현 방법 두가지 있음
(1) 모든 좌표에서 우,하만 보기 (2) 모든 좌표에서 네방향 다 보지만 내가 클 때만 처리

2. 방향별 딕셔너리 만들어서 정해진 방향대로 bfs에서 보는 로직
'''

# 격자의 크기, 벽의 개수, 원하는 사무실의 시원함 정도
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
office = []
air_con = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            office.append((i, j))

        elif arr[i][j] == 2:
            air_con.append((3, i, j))

        elif arr[i][j] == 3:
            air_con.append((0, i, j))

        elif arr[i][j] == 4:
            air_con.append((1, i, j))

        elif arr[i][j] == 5:
            air_con.append((2, i, j))

# 상,우,하,좌
dic = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
wall = [[[0, 0, 0, 0] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, s = map(int, input().split())
    x,y = x-1,y-1
    if s == 0:
        wall[x][y][0] = 1
        wall[x - 1][y][2] = 1
    else:
        wall[x][y][3] = 1
        wall[x][y - 1][1] = 1

temp = [[0] * N for _ in range(N)]
check = {0: ((3, 0), (0,), (1, 0)), 1: ((0, 1), (1,), (2, 1)), 2: ((3, 2), (2,), (1, 2)), 3: ((0, 3), (3,), (2, 3))}

# ============================================================
from collections import deque

def bfs(d, i, j):
    v = [[0] * N for _ in range(N)]
    di, dj = dic[d]
    si, sj = i + di, j + dj
    q = deque([(si, sj,5)])
    temp[si][sj] +=5
    v[si][sj] = 1

    while q:
        ci, cj, amount = q.popleft()
        if amount == 1:
            break

        for dirs in check[d]:
            si, sj = ci, cj
            for dir in dirs:
                di, dj = dic[dir]
                ni, nj = si + di, sj + dj
                if 0 <= ni < N and 0 <= nj < N and wall[si][sj][dir] == 0 and v[ni][nj] == 0:
                    si, sj = ni, nj
                else:
                    break
            else:
                q.append((ni, nj,amount-1))
                v[ni][nj] = 1
                temp[ni][nj] += amount-1

for time in range(101):
    for i,j in office:
        if temp[i][j]<K:
            break
    else:
        print(time)
        break

    for d, i, j in air_con:
        bfs(d, i, j)

    new_temp=[row[:] for row in temp]

    for i in range(N):
        for j in range(N):
            for num in (1,2):
                di,dj=dic[num]
                ni,nj=i+di,j+dj
                if 0<=ni<N and 0<=nj<N and wall[i][j][num]==0:
                    diff=(abs(temp[i][j]-temp[ni][nj]))//4
                    if temp[i][j]>temp[ni][nj]:
                        new_temp[i][j]-=diff
                        new_temp[ni][nj]+=diff
                    else:
                        new_temp[ni][nj]-=diff
                        new_temp[i][j]+=diff

    temp=new_temp

    for j in range(N):
        if temp[0][j]>0:
            temp[0][j]-=1
        if temp[N-1][j]>0:
            temp[N-1][j]-=1

    for i in range(1,N-1):
        if temp[i][N-1]>0:
            temp[i][N-1]-=1
        if temp[i][0]>0:
            temp[i][0]-=1

else:
    print(-1)

'''
B23289 온풍기 안녕! / 2025-03-19 / 체감 난이도 : 골드 1
소요 시간 : 2시간 40분 / 시도 : 2회

[0] 총평
- 큐빙 풀 때도 느꼈는데.. 노가다하는 스스로를 안타깝게 생각하지 말자
이게 맞아? 생각하면서 코드를 짜면 자신감이 떨어지고 코드에 대한 확신이 사라진다 -> 그럼 실수 와장창에 엣지 와장창 걸림
멋진 방법이 아니여도 괜찮다 안전한 방법으로 밀고 나가면 된다

[1] 타임라인
1. 문제 이해 & 구상 & 입력 받기 (35분)

2. 온풍기 바람 구현 (30분)
-> 방향마다 다른 거 구현하다가 멍~해지고 헷갈리기 시작
이때 멈춰서 싹 지우고 종이 구상으로 다시 돌아갔는데 이게 아주 좋았음 !!!!
** 너무 길어질 땐 무조건 stop, 그리고 종이에서 다시 생각하기

3. 온풍기 바람 재구현 (20분)

4. 나머지 구현 (20분)

5. 디버깅 (25분)
-> tp 배열에서 온풍기 방향 가져와야 하는데 arr로 잘못 씀
-> index 에러가 떠서 온풍기 돌릴 때 범위 체크 안 해준 거 발견
여기서 좀만 더 생각했다면 cnt가 0일 때 나가는 코드도 넣었을 텐데.. 이래서 에러뜨면 그거만 고치는게 아니라 또 놓친 거 있는지 꼼꼼히 생각해야함 !!!
-> 오픈테케 몇개 틀린 거 발견
다행히 문제에서 배열이 주어졌고 온풍기 확산이 이상하게 되는 거 확인
나는 온풍기가 있는 곳은 온도가 없다고 생각해서 -1로 표시했는데 문제 다시 읽어보니 아니였음 !

6. 틀렸습니다 -> 재디버깅 (20분)
-> 로직 다시 생각해보니까 온도 5에서 시작해서 하나씩 줄어들면서 퍼지다가 0이되면 더 하면 안 되는데 이걸 멈춰주는 코드가 없다는 것을 발견
주어진 예제로 디버깅할 엄두가 안 나서 로직 검토를 한 건데 예전보다 훨씬 빠르게 발견..
** 냅다 디버깅보다 로직 검토가 훨씬 더더더 중요하다는 것을 한번 더 느낌 !


[2] 배운점 및 실수한 점

[3] 시간 복잡도
최대 100번 x (온풍기 개수마다 blow + R*C 온도 조절) <- 이 부분이 젤 크니까
대충 요런 느낌 100 x (400 x (1+3+5+7+9))

'''

from collections import deque

# 방향별 확산 가능한 위치를 모든 케이스 나눠서 처리
def blow_r(si, sj):
    q = deque()
    q.append((si, sj, 5))
    v = [[0] * C for _ in range(R)]   # 같은 온풍기에서는 두번 처리해주면 안 되니까 visited 확인
    v[si][sj] = 1

    while q:
        ci, cj, cnt = q.popleft()
        if cnt == 0:    # 0초가 됐다는 건 이제 확산 그만 해야되는 거 !
            break

        arr[ci][cj] += cnt
        di, dj = -1, 1
        if 0<=ci+di<R and 0<=cj+dj<C:
            if wall[ci][cj][0] != 1 and wall[ci - 1][cj][1] != 1 and v[ci + di][cj + dj] == 0:
                q.append((ci + di, cj + dj, cnt - 1))
                v[ci + di][cj + dj] = 1

        di, dj = 0, 1
        if 0 <= ci + di < R and 0 <= cj + dj < C:
            if wall[ci][cj][1] != 1 and v[ci + di][cj + dj] == 0:
                q.append((ci + di, cj + dj, cnt - 1))
                v[ci + di][cj + dj] = 1

        di, dj = 1, 1
        if 0 <= ci + di < R and 0 <= cj + dj < C:
            if wall[ci + 1][cj][0] != 1 and wall[ci + 1][cj][1] != 1 and v[ci + di][cj + dj] == 0:
                q.append((ci + di, cj + dj, cnt - 1))
                v[ci + di][cj + dj] = 1

def blow_l(si, sj):
    q = deque()
    q.append((si, sj, 5))
    v = [[0] * C for _ in range(R)]
    v[si][sj] = 1

    while q:
        ci, cj, cnt = q.popleft()
        arr[ci][cj] += cnt
        if cnt == 0:
            break

        di, dj = -1, -1
        if 0 <= ci + di < R and 0 <= cj + dj < C:
            if wall[ci][cj][0] != 1 and wall[ci - 1][cj-1][1] != 1 and v[ci + di][cj + dj] == 0:
                q.append((ci + di, cj + dj, cnt - 1))
                v[ci + di][cj + dj] = 1

        di, dj = 0, -1
        if 0 <= ci + di < R and 0 <= cj + dj < C:
            if wall[ci][cj-1][1] != 1 and v[ci + di][cj + dj] == 0:
                q.append((ci + di, cj + dj, cnt - 1))
                v[ci + di][cj + dj] = 1

        di, dj = 1, -1
        if 0 <= ci + di < R and 0 <= cj + dj < C:
            if wall[ci + 1][cj][0] != 1 and wall[ci + 1][cj-1][1] != 1 and v[ci + di][cj + dj] == 0:
                q.append((ci + di, cj + dj, cnt - 1))
                v[ci + di][cj + dj] = 1

def blow_u(si, sj):
    q = deque()
    q.append((si, sj, 5))
    v = [[0] * C for _ in range(R)]
    v[si][sj] = 1

    while q:
        ci, cj, cnt = q.popleft()
        arr[ci][cj] += cnt
        if cnt == 0:
            break

        di, dj = -1, -1
        if 0 <= ci + di < R and 0 <= cj + dj < C:
            if wall[ci][cj-1][0] != 1 and wall[ci][cj-1][1] != 1 and v[ci + di][cj + dj] == 0:
                q.append((ci + di, cj + dj, cnt - 1))
                v[ci + di][cj + dj] = 1

        di, dj = -1,0
        if 0 <= ci + di < R and 0 <= cj + dj < C:
            if wall[ci][cj][0] != 1 and v[ci + di][cj + dj] == 0:
                q.append((ci + di, cj + dj, cnt - 1))
                v[ci + di][cj + dj] = 1

        di, dj = -1,1
        if 0 <= ci + di < R and 0 <= cj + dj < C:
            if wall[ci][cj][1] != 1 and wall[ci][cj+1][0] != 1 and v[ci + di][cj + dj] == 0:
                q.append((ci + di, cj + dj, cnt - 1))
                v[ci + di][cj + dj] = 1

def blow_d(si, sj):
    q = deque()
    q.append((si, sj, 5))
    v = [[0] * C for _ in range(R)]
    v[si][sj] = 1

    while q:
        ci, cj, cnt = q.popleft()
        arr[ci][cj] += cnt

        if cnt == 0:
            break

        di, dj = 1, -1
        if 0 <= ci + di < R and 0 <= cj + dj < C:

            if wall[ci+1][cj-1][0] != 1 and wall[ci][cj-1][1] != 1 and v[ci + di][cj + dj] == 0:
                q.append((ci + di, cj + dj, cnt - 1))
                v[ci + di][cj + dj] = 1

        di, dj = 1,0
        if 0 <= ci + di < R and 0 <= cj + dj < C:
            if wall[ci+1][cj][0] != 1 and v[ci + di][cj + dj] == 0:
                q.append((ci + di, cj + dj, cnt - 1))
                v[ci + di][cj + dj] = 1

        di, dj = 1,1
        if 0 <= ci + di < R and 0 <= cj + dj < C:
            if wall[ci][cj][1] != 1 and wall[ci+1][cj+1][0] != 1 and v[ci + di][cj + dj] == 0:
                q.append((ci + di, cj + dj, cnt - 1))
                v[ci + di][cj + dj] = 1

# =======================================

# 행, 열, 조사하는 모든 칸 온도 K이상이여야
R,C,K=map(int,input().split())
tp=[list(map(int,input().split())) for _ in range(R)]
# 온도 배열 즉 이게 메인이지
arr=[[0]*C for _ in range(R)]

# 온풍기를 담는 배열
on=[]
# 체크해야할 위치 담는 배열
check=[]
for i in range(R):
    for j in range(C):
        if tp[i][j] != 0 and tp[i][j] != 5:
            on.append((i,j))

        if tp[i][j] == 5:
            check.append((i,j))

W=int(input())
# wall 에는 한 좌표에서 위 경게 (t가 0일 때) // 오른쪽 경계 (t가 1일때) 이렇게 두개가 있음
wall=[[[0,0] for _ in range(C)] for _ in range(R)]

for _ in range(W):
    x,y,t=map(int,input().split())
    x,y=x-1,y-1

    if t==0:
        wall[x][y][0]=1
    else:
        wall[x][y][1]=1

# ============================== 초기 입력 받았고
choc=0
dic={1:(0,1),2:(0,-1),3:(-1,0),4:(1,0)}

while True:
    if choc>100:
        print(101)
        break
    # [1] 온풍기 바람이 분다
    for i,j in on:
        dr=tp[i][j]
        di,dj=dic[dr]
        si,sj=i+di,j+dj

        if dr == 1:
            blow_r(si,sj)
        elif dr == 2:
            blow_l(si,sj)
        elif dr==3:
            blow_u(si,sj)
        else:
            blow_d(si,sj)

    # [2] 온도가 조절 된다
    # 나는 wall에 위,오른쪽 경계선을 체크했으니까 모든 좌표에 대해서 그 두 방향으로 확인하면
    # 모든 두개 쌍 (?)을 중복 없이 처리할 수 있다는 것을 그려보며 발견

    new_arr=[row[:] for row in arr]
    for i in range(R):
        for j in range(C):
            di,dj = -1,0  # 한 좌표를 기준으로 위에 있는 칸이랑 비교
            ni,nj=i+di,j+dj
            if 0<=ni<R and 0<=nj<C and wall[i][j][0]==0:
                if arr[ni][nj]>arr[i][j]:
                    new_arr[ni][nj]-=(arr[ni][nj]-arr[i][j]) // 4
                    new_arr[i][j]+=(arr[ni][nj] - arr[i][j]) // 4
                else:
                    new_arr[i][j]-=(arr[i][j]-arr[ni][nj]) // 4
                    new_arr[ni][nj]+=(arr[i][j]-arr[ni][nj]) // 4

            di,dj = 0,1  # 오른쪽에 있는 칸이랑 비교
            ni, nj = i + di, j + dj
            if 0<=ni<R and 0<=nj<C and wall[i][j][1]==0:
                if arr[ni][nj]>arr[i][j]:
                    new_arr[ni][nj]-=(arr[ni][nj]-arr[i][j]) // 4
                    new_arr[i][j]+=(arr[ni][nj] - arr[i][j]) // 4
                else:
                    new_arr[i][j]-=(arr[i][j]-arr[ni][nj]) // 4
                    new_arr[ni][nj]+=(arr[i][j]-arr[ni][nj]) // 4

    arr=new_arr

    # [3] 테두리에서 1 이상이면 -1씩 감소한다
    for j in range(C):
        if arr[0][j]>0:
            arr[0][j]-=1

    for i in range(1,R):
        if arr[i][C-1]>0:
            arr[i][C-1]-=1

    for j in range(0,C-1):
        if arr[R-1][j]>0:
            arr[R-1][j]-=1

    for i in range(1,R-1):
        if arr[i][0]>0:
            arr[i][0]-=1

    # [4] 초콜릿 먹는다
    choc+=1

    # [5] 조사하는 모든 칸 온도 확인한다
    for i,j in check:
        if arr[i][j]<K:
            break
    else:
        print(choc)
        break
