# 같은 모양인지 판단을 어떻게 할 것인가?
# 8:37 ~

# 1. 같은 모양을 어떻게 판단할 것인가

# 2. 하나의 모양은 어떻게 식별할 것인가?
# 8방향 bfs로

# 같은 모양과 수이면 같은 클러스터
# 미리 만들어진 거 8방향으로 회전해보고 똑같은 거 없으면 새로운 알파벳으로 칠한다

# 기준만 잡고 상대좌표로 비교하기
# 모든 점을 기준좌표로 삼아보고
# 기준은 좌 상단에 있는 좌표 -> 정렬할 필요없이 자동으로 됨

M = int(input())
N = int(input())

arr = [list(map(int, input())) for _ in range(N)]
v = [[0] * M for _ in range(N)]

from collections import deque

def bfs(i, j):
    v[i][j] = 1
    q = deque([(i, j)])
    shape = [(0, 0)]
    loc = [(i, j)]

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1 and v[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = 1
                shape.append((ni - i, nj - j))
                loc.append((ni, nj))

    return shape, loc

def rotate(lst,num):
    if num == 0:
        for idx,(x,y) in enumerate(lst):
            lst[idx]=(-y,x)
        return lst
    else:
        for idx,(x,y) in enumerate(lst):
            lst[idx]=(-x,y)
        return lst

def try_already_exist(loc):
    if not already_exist: return 0
    for key, val in already_exist.items():
        if len(val) != len(loc): continue

        for cnt in range(8):
            loc_st = set(loc)
            for pi, pj in loc:
                # pi,pj를 기준으로 잡고 나머지와 상대좌표 비교해볼건데
                for di, dj in val:
                    if (pi + di, pj + dj) not in loc_st: break
                else:
                    # 만약 한 번도 break가 안 됐으면 된 거니까
                    return key
            if cnt == 4: num = 1
            else: num = 0
            val=rotate(val,num)
            loc=rotate(loc,num)

    return 0

already_exist = {}
alp = 97

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and v[i][j] == 0:
            shape, loc = bfs(i, j)
            final_loc=loc[:]
            # 동일한 모양이 없다면
            result = try_already_exist(loc)

            if not result:
                for x, y in final_loc:
                    arr[x][y] = chr(alp)
                already_exist[alp] = shape
                alp += 1
            else:
                for x, y in final_loc:
                    arr[x][y] = chr(result)

for row in arr:
    print(*row)
