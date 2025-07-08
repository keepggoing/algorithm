'''2차풀이
[0] 타임라인
구상 (30분)
구현 (25분)
디버깅 (5분)

[1] 실수한점
1. bfs에서 visited 처리 안함, 체크리스트 추가하기
2. 중간 위치를 안 칠해줌

[2] 배운점
1. 음수는 절댓값 사용하면 양수랑 같은 역할을, 하지만 음수일 때만 따로 추가적인 처리 하기 좋다는 점 기억하기
2. 될 때까지 1,2,3 단계를 반복하라는 건지, 한 단계를 반복하라는 건지 문제 이해 잘 해야함
'''
# N은 행, M은 열, K는 정령의 수
N, M, K = map(int, input().split())
arr = [[1] + [0] * M + [1] for _ in range(N + 3)] + [[1] * (M + 2)]

# ==============================================
# 북 동 남 서
dic = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
score = 0

from collections import deque


def bfs(si, sj):
    q = deque([(si, sj)])
    v = [[1] + [0] * M + [1] for _ in range(N + 3)] + [[1] * (M + 2)]
    v[si][sj] = 1
    mx=si

    while q:
        ci, cj = q.popleft()                    # pop하고
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):   # 네방향 보는데
            ni, nj = ci + di, cj + dj

            if arr[ci][cj] < 0:                 # 음수면
                if arr[ni][nj] != 1 and arr[ni][nj] != 0 and v[ni][nj]==0:   # 벽이랑 빈 곳만 아니면 갈 수 있음
                    q.append((ni, nj))
                    mx=max(mx,ni)
                    v[ni][nj] = 1

            else:
                if abs(arr[ni][nj]) == abs(arr[ci][cj]) and v[ni][nj]==0:
                    q.append((ni, nj))
                    mx=max(mx,ni)
                    v[ni][nj] == 1
    return mx-2


for k in range(2, K + 2):
    ci = 1
    cj, dr = map(int, input().split())

    while True:
        flag = False

        # 남쪽으로
        for di, dj in ((1, -1), (2, 0), (1, 1)):
            ni, nj = ci + di, cj + dj
            if arr[ni][nj] != 0:
                break
        else:
            ci += 1
            flag = True
            continue

        # 서쪽으로
        for di, dj in ((-1, -1), (0, -2), (1, -2), (1, -1), (2, -1)):
            ni, nj = ci + di, cj + dj
            if arr[ni][nj] != 0:
                break
        else:
            ci, cj = ci + 1, cj - 1
            dr = (dr - 1) % 4
            flag = True
            continue

        # 동쪽으로
        for di, dj in ((-1, 1), (0, 2), (1, 1), (1, 2), (2, 1)):
            ni, nj = ci + di, cj + dj
            if arr[ni][nj] != 0:
                break
        else:
            ci, cj = ci + 1, cj + 1
            dr = (dr + 1) % 4
            flag = True
            continue

        if not flag:
            break

    # 이렇게 해서 나온 게 최종 ci,cj,dr
    if ci < 4:
        # 비우기
        arr = [[1] + [0] * M + [1] for _ in range(N + 3)] + [[1] * (M + 2)]
        continue

    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1), (0,0)):
        ni, nj = ci + di, cj + dj
        if (di,dj) == dic[dr]:
            arr[ni][nj] = -k
        else:
            arr[ni][nj] = k

    #for row in arr:
    #    print("".join(f'{x:4}' for x in row))
    #print("=======")

    score += bfs(ci, cj)

print(score)

'''
[체감 난이도 & 총평]
골 1

[시간복잡도]
K x R x C 1000x70x70 ㄱㅊ

[타임라인]
1400 - 1430 구상
1430 - 1545 score 함수 빼고 구현
1545 - 1710 score 함수 구현 ..
1716 1차 제출 -> 틀렸습니다

[배운점 및 실수한 점]
- 일단 문제 이해 잘못함 -> 잘못된 구현에 계속 시간 쓰고 있었던 거니까.. 얼마나 아깝니 문제 이해는 항상 1순위
" 골렘은 다음과 같은 우선순위로 이동합니다. 더 이상 움직이지 못할 때까지 해당 과정을 반복합니다 "
과정 == (1) 남쪽으로 한 칸 내려갑니다 -> (2) 안 되면 서쪽으로 -> (3) 안 되면 동쪽으로
나는 남쪽 안 되면 서서서서서서 안 되면 동동동동 이렇게 구현했었는데 그게 아니라 남 서 동이 계속 반복되는 것

- 잘못 옮겨적은 거 있었음 하드코딩 옮겨적을 땐 꼭 조심해야하고 아닐 거라고 생각되는 부분도 다 검토해야해
def right(ci, cj, cd):
    check = [(ci-1,cj+1),(ci+1,cj+1),(ci,cj+2),(ci+2,cj+1),(ci+1,cj+2)]         # 옮겨적기 실수 부들부들

- 내려가는 거 어떻게 구현할지 생각이 안 나서 오래걸림 -> 팀원들 코드 잘 보기

'''

from collections import deque

def score(si, sj):
    mx = si + 1                                 # 행 최대는 중심에서 하나 내려간 거

    q = deque([(si, sj)])
    v = [[0] * M for _ in range(N)]
    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if arr[ni][nj]!=0 and arr[ni][nj]!=-1 and v[ni][nj] == 0:   # 0 아니고 범위 밖 아니고 방문 안 했으면
                if exit[ci][cj]!=1 and arr[ni][nj] != arr[ci][cj]:     # 출구가 아닌데 같은 숫자가 아니라면 안돼 !
                    continue
                q.append((ni, nj))
                v[ni][nj] = 1
                mx = max(mx, ni)
    return mx - 2

# ====================================================
# N은 행, M은 열, K는 정령의 수
N,M,K=map(int,input().split())
arr=[[-1]+[0]*M+[-1] for _ in range(N+3)] + [[-1]*(M+2)]            # 위에 행 3개 추가, 양 옆에 -1로 열 추가, -1로만 구성된 마지막 행 추가
N+=4
M+=2

# ====================================================
# 상 우 하 좌
dic={0:(-1,0),1:(0,1),2:(1,0),3:(0,-1)}
ans=0
color=1

def down(ci, cj, cd):
    check = [(ci + 1, cj - 1), (ci + 2, cj), (ci + 1, cj + 1)]

    for x, y in check:
        if arr[x][y] != 0:
            return False, ci, cj, cd
    else:
        ci += 1
        return True,ci,cj,cd


def left(ci, cj, cd):
    check = [(ci, cj - 2), (ci - 1, cj - 1), (ci + 1, cj - 1), (ci + 1, cj - 2), (ci + 2, cj - 1)]

    for x, y in check:
        if arr[x][y] != 0:
            return False, ci, cj, cd
    else:
        ci +=1
        cj -=1
        cd = (cd - 1) % 4
        return True, ci, cj, cd

def right(ci, cj, cd):
    check = [(ci-1,cj+1),(ci+1,cj+1),(ci,cj+2),(ci+2,cj+1),(ci+1,cj+2)]         # 옮겨적기 실수 부들부들

    for x, y in check:
        if arr[x][y] != 0:
            return False, ci, cj, cd
    else:
        ci +=1
        cj +=1
        cd = (cd+1) % 4
        return True, ci, cj, cd

# ===============================================================
exit=[[-1]+[0]*(M-2)+[-1] for _ in range(N-1)] + [[-1]*(M+2)]
for _ in range(K):
    ci=1
    cj,cd=map(int,input().split())
    fg=False

    while not fg:                                       # 다 안 될 때까지 반복해
        flag,ci,cj,cd=down(ci,cj,cd)
        if flag:
            continue
        else:
            flag,ci,cj,cd=left(ci,cj,cd)
            if flag:
                continue
            else:
                flag, ci, cj, cd = right(ci, cj, cd)
                if flag:
                    continue
                else:
                    fg=True
    if 0<=ci<4:
        arr=[[-1]+[0]*(M-2)+[-1] for _ in range(N-1)] + [[-1]*(M+2)]
        exit=[[-1]+[0]*(M-2)+[-1] for _ in range(N-1)] + [[-1]*(M+2)]
        continue
    else:
        arr[ci][cj] = color
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            arr[ci + di][cj + dj] = color
        exit[ci + dic[cd][0]][cj + dic[cd][1]] = 1                      # 출구는 따로 관리해
        color += 1

    ans+=score(ci,cj)

print(ans)