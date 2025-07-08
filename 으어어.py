'''
[0] 아리 위치
si,sj=0,0
** 틀린 지점 1 : 이거부터 잘못썼었네... 좌우 바꿔썼음
# 상 하 좌 우
dir=[(-1,0),(1,0),(0,-1),(0,1)]
dr=1

[1] 명령 하나 할 때마다 해야하는 일?
F 1칸 전진 ( 범위 밖이면 제자리에 머문다 )
L 방향만 왼쪽으로 90도 전환
R 방향만 오른쪽으로 90도 전환

-1 ) 아리 움직인다
-2 ) 새로 도착한 곳이 스위치가 있는 칸이면 스위치 on, 상하좌우대각선 모두 스위치 on
- 시작 좌표에 스위치가 있을 수도 있지 않음?
- 스위치 킬 때 상하좌우대각선에 스위치가 있는 상태면? on으로 덮어씌워지지 않음?
따로 관리해야겠다
-3 ) 좀비들이 한 칸씩 전진한다 ( 범위 밖이면 반대 방향으로 바꾼다 )

불이 꺼져있는 칸에서 좀비를 보면 기절 -> 바로 종료
전진하고 나서도 혹시 마주치면 -> 바로 종료

불이 켜져있거나 (상하좌우 밝혀진) 스위치가 있는 칸 ( 이것도 걍 밝혀진 )에서는 기절 안함

이렇게 배열로 관리하면 문제가 생길까?
좀비가 두마리인데, 같은 곳에 있다면.. 하나 지나가면서 좀비를 없애버릴 수도 있잖아

** 2차원 배열에 기록하고 다니면 덮어씌워질 가능성이 있어서 항상 조심해야함
** 같은 변수 중복으로 안 쓰도록 조심해야함
'''

from collections import deque

# 정사각형 한 변의 길이
N = int(input())

# 명령들
A = list(input())

# 현재 위치 기록
arr = [list(input()) for _ in range(N)]

# 불 켜진 거 기록
v = [[0] * N for _ in range(N)]

# 큐는 좀비큐야 !!!!!
q = deque()

# 스위치 있는 곳
sw = []

# [0] 초기 상태
si, sj = 0, 0
# 상, 하, 좌, 우
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dr = 1

# arr에서는 좀비랑 아리만 확인한다
for i in range(N):
    for j in range(N):
        # 좀비면 좀비 큐에 다 넣는다
        if arr[i][j] == "Z":
            q.append((i, j, dr))

        # 스위치 있는 거 다 넣는다
        elif arr[i][j] == "S":
            sw.append((i, j))

# si,sj는 항상 아리의 위치
# dr도 아리 방향
for alp in A:
    if alp == 'F':
        ni, nj = si + dir[dr][0], sj + dir[dr][1]
        if 0 <= ni < N and 0 <= nj < N:
            si, sj = ni, nj

            # 만약 스위치이면? 스위치 1차원 배열에 다 넣고 관리를 해야한다 !
            if (si,sj) in sw:
                v[si][sj] = 1
                for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)):
                    ti, tj = si + di, sj + dj
                    if 0 <= ti < N and 0 <= tj < N:
                        # 불을 켠다
                        v[ti][tj] = 1

        # 아리 위치 = 불이 꺼진 곳 = 좀비가 있어
        found=False
        for r,c,m in q:
            if r==si and c==sj and v[si][sj]==0:
                print("Aaaaaah!")
                found=True
                break
        if found:
            break

    elif alp == 'L':
        dr = [2, 3, 1, 0][dr]

    elif alp == 'R':
        dr = [3, 2, 0, 1][dr]

    # 다 하고 나서 좀비가 움직인다
    for _ in range(len(q)):
        ci, cj, d = q.popleft()
        ni, nj = ci + dir[d][0], cj + dir[d][1]
        if 0 <= ni < N and 0 <= nj < N:
            # 원래 있었던 곳은 없었던 거 처럼
            q.append((ni, nj, d))
        else:
            # 상은 하로, 하는 상으로, 좌는 우로, 우는 좌로
            d = [1, 0, 3, 2][d]
            q.append((ci, cj, d))


    # 다 움직이고 나서 좀비의 위치랑 나랑 같으면? 끝내야함
    found = False
    for r, c, m in q:
        if r == si and c == sj and v[si][sj] == 0:
            print("Aaaaaah!")
            found = True
            break
    if found:
        break
else:
    print("Phew...")
