''' 2차 풀이
[1] 소요시간 : 1시간 ( 20분 구상 - 40분 구현 )
[2] 고려한 점 : 1차풀이를 하면서 방향별로 함수를 따로 만들어 처리를 하니까 디버깅이 쉽지 않았음
공통적인 move 함수를 만드는 것을 고려했고, move 함수의 결과에 따라 아예 백트래킹 함수로 넘기지 않을 수도 있도록
구현함
[3] 실수 : 백트래킹 함수에서 cnt를 증가시키지 않아서 무한루프 에러
[4] 시간복잡도 : 4^10 -> 2^20 -> 10^6 정도로 오케이
'''

def move(si,sj,di,dj):
    back=-1
    for mul in range(1,10):
        ni,nj=si+di*mul,sj+dj*mul
        if arr[ni][nj] == "#":
            return mul+back

        elif arr[ni][nj] == "O":
            return mul

        elif arr[ni][nj] == "R" or arr[ni][nj] == "B":
            back-=1

def btk(cnt, ri, rj, bi, bj):
    global mn

    if cnt == 11:
        return

    if cnt > mn:  # 이미 더 크면 가지치기
        return

    for i in range(4):
        di, dj = dic[i]
        rd = move(ri, rj, di, dj)
        bd = move(bi, bj, di, dj)

        # 둘다 움직이는 거리가 0이면 안 해봐도 되지
        if rd == 0 and bd == 0:
            continue

        nri, nrj = ri + di * rd, rj + dj * rd
        nbi, nbj = bi + di * bd, bj + dj * bd

        if (nbi,nbj) == (ei,ej):
            continue
        else:
            if (nri,nrj) == (ei,ej):
                mn=min(cnt,mn)
                return

        # 움직였으니까
        arr[ri][rj], arr[bi][bj] = ".", "."
        arr[nri][nrj], arr[nbi][nbj] = "R", "B"
        btk(cnt+1, nri, nrj, nbi, nbj)
        # 원상복구
        arr[nri][nrj], arr[nbi][nbj] = ".", "."
        arr[ri][rj], arr[bi][bj] = "R", "B"

# N은 행, M은 열
N,M=map(int,input().split())
arr=[list(input()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == "R":
            ri,rj=i,j

        if arr[i][j] == "B":
            bi,bj=i,j

        if arr[i][j] == "O":
            ei,ej=i,j

# =======
# 상,하,좌,우
dic={0:(-1,0),1:(1,0),2:(0,-1),3:(0,1)}
mn=11
btk(1,ri,rj,bi,bj)

if mn == 11:
    print(-1)
else:
    print(mn)

'''
B13460 구슬 탈출 2 / 2025-03-14 / 체감 난이도 : 골드 2
소요 시간 : 3시간 - 다 지우고 재시도 3시간 / 시도 : 3회

[0] 총평
- 백트래킹 구상을 다 안 하고 들어가니 꼬임
백트래킹 문제를 풀 땐 꼭 꼭 트리를 그리고 시작할 것 !

- 백트래킹의 기본 개념은 더이상 의심하면 안됨
처음에 풀 때 1번씩 다 하고, 2번씩 다하고 이렇게 하고 싶다고 생각하고 백트래킹을 쓰려고 했음
1번 쭉 보고 2번 쭉 보고 ~ <- 이건 bfs인 거고.. 백트래킹은 어쨋든 맨 밑에까지 가야함 ( 중간에 플래그로 끊을 순 있지만 )

- 배열을 다 들고 다니면서 원상복구를 해주니까.. 시간이 엄청 오래 걸림
배열을 굳이 다 복사할 필요가 있을까? 중요한 건 빨간 구슬과 파란 구슬의 위치 뿐인데 !

[1] 타임라인
1. 문제 이해 및 구상 (1시간)
2. 구현 (1시간)
3. 디버깅 (1시간)
-> R을 A라고 씀
-> 구상 노트엔 잘 썼는데 범위 잘못 옮겨적음
머리가 꽉찬 기분이 들때 디버깅하면 너무 오래걸림.. 꼭 디버깅 전에는 환기를 할 것
+ 코드가 길어지면 디버깅 쉽지 않음 **일반화**

[2] 배운점 및 실수한 점
- move 함수를 하나로 만들었다가 여러개로 만들었다가 여러 구상을 하다가 코드를 짜니까 짬뽕이 됨
하나의 방법을 골랐으면 머리 비우고 그거로 밀고 나가기

- 결국 실패 요인은 global 로 ri,rj,bi,bj를 관리하고 배열 복사로 상태를 원상복구 하니까..
정작 중요한 ri,rj,bi,bj는 원상복구가 안 되었던 것 !

문제에서 내가 집중해서 관리해야하는 것이 무엇인지 생각하는 것은 기본 중에 기본임 !!!!

- 백트래킹 종료조건의 위치는 중요함 !
11번 부터 안됨 -> 11번은 해볼 필요 없음 -> cnt 10번까지 해보면 됨
cnt 종료조건보다 위에서 성공 여부를 확인해야함
왜냐? 10번까지 돌았을 때의 결과를 확인하고 끝내야지 10번됐다고 바로 return하면 안됨

'''
def move_left(ri, rj, bi, bj):
    # 현재 구슬의 위치를 매개변수로 가져옴
    # 그렇다면 맵에도 동일하게 반영되어있음
    # 원상복귀할 때 맵에 바꿔주면 됨

    di, dj = 0, -1
    good = 0
    gd = []

    if ri == bi and rj < bj:
        while True:
            ni, nj = ri + di, rj + dj
            if arr[ni][nj] == ".":
                arr[ri][rj] = "."
                ri, rj = ni, nj
                arr[ri][rj] = "R"
            elif arr[ni][nj] == "O":
                arr[ri][rj] = "."
                gd.append("R")
                break
            else:
                # 벽이거나 다른 거면
                break
        while True:
            ni, nj = bi + di, bj + dj
            if arr[ni][nj] == ".":
                arr[bi][bj] = "."
                bi, bj = ni, nj
                arr[bi][bj] = "B"
            elif arr[ni][nj] == "O":
                arr[bi][bj] = "."
                gd.append("B")
                break
            else:
                # 벽이거나 다른 거면
                break

    else:  # 아닐 땐 뭐부터 해도 상관없음
        while True:
            ni, nj = bi + di, bj + dj
            if arr[ni][nj] == ".":
                arr[bi][bj] = "."
                bi, bj = ni, nj
                arr[bi][bj] = "B"
            elif arr[ni][nj] == "O":
                arr[bi][bj] = "."
                gd.append("B")
                break
            else:
                # 벽이거나 다른 거면
                break

        while True:
            ni, nj = ri + di, rj + dj
            if arr[ni][nj] == ".":
                arr[ri][rj] = "."
                ri, rj = ni, nj
                arr[ri][rj] = "R"
            elif arr[ni][nj] == "O":
                arr[ri][rj] = "."
                gd.append("R")
                break
            else:
                # 벽이거나 다른 거면
                break

    if "B" in gd:
        return ri, rj, bi, bj, -1

    # 위에 안 걸리고 여기에 걸린다는 건 A만 있다는 거니까
    elif "R" in gd:
        return ri, rj, bi, bj, 1

    else:
        return ri, rj, bi, bj, 0

def move_right(ri, rj, bi, bj):
    # 현재 구슬의 위치를 매개변수로 가져옴
    # 그렇다면 맵에도 동일하게 반영되어있음
    # 원상복귀할 때 맵에 바꿔주면 됨

    di, dj = 0, 1
    good = 0
    gd = []

    if ri == bi and rj > bj:
        while True:
            ni, nj = ri + di, rj + dj
            if arr[ni][nj] == ".":
                arr[ri][rj] = "."
                ri, rj = ni, nj
                arr[ri][rj] = "R"
            elif arr[ni][nj] == "O":
                arr[ri][rj] = "."
                gd.append("R")
                break
            else:
                # 벽이거나 다른 거면
                break
        while True:
            ni, nj = bi + di, bj + dj
            if arr[ni][nj] == ".":
                arr[bi][bj] = "."
                bi, bj = ni, nj
                arr[bi][bj] = "B"
            elif arr[ni][nj] == "O":
                arr[bi][bj] = "."
                gd.append("B")
                break
            else:
                # 벽이거나 다른 거면
                break

    else:  # 아닐 땐 뭐부터 해도 상관없음
        while True:
            ni, nj = bi + di, bj + dj
            if arr[ni][nj] == ".":
                arr[bi][bj] = "."
                bi, bj = ni, nj
                arr[bi][bj] = "B"
            elif arr[ni][nj] == "O":
                arr[bi][bj] = "."
                gd.append("B")
                break
            else:
                # 벽이거나 다른 거면
                break

        while True:
            ni, nj = ri + di, rj + dj
            if arr[ni][nj] == ".":
                arr[ri][rj] = "."
                ri, rj = ni, nj
                arr[ri][rj] = "R"
            elif arr[ni][nj] == "O":
                arr[ri][rj] = "."
                gd.append("R")
                break
            else:
                # 벽이거나 다른 거면
                break

    if "B" in gd:
        return ri, rj, bi, bj, -1

    # 위에 안 걸리고 여기에 걸린다는 건 A만 있다는 거니까
    elif "R" in gd:
        return ri, rj, bi, bj, 1

    else:
        return ri, rj, bi, bj, 0


def move_up(ri, rj, bi, bj):
    # 현재 구슬의 위치를 매개변수로 가져옴
    # 그렇다면 맵에도 동일하게 반영되어있음
    # 원상복귀할 때 맵에 바꿔주면 됨

    di, dj = -1,0
    good = 0
    gd = []

    if rj == bj and ri < bi:
        while True:
            ni, nj = ri + di, rj + dj
            if arr[ni][nj] == ".":
                arr[ri][rj] = "."
                ri, rj = ni, nj
                arr[ri][rj] = "R"
            elif arr[ni][nj] == "O":
                arr[ri][rj] = "."
                gd.append("R")
                break
            else:
                # 벽이거나 다른 거면
                break
        while True:
            ni, nj = bi + di, bj + dj
            if arr[ni][nj] == ".":
                arr[bi][bj] = "."
                bi, bj = ni, nj
                arr[bi][bj] = "B"
            elif arr[ni][nj] == "O":
                arr[bi][bj] = "."
                gd.append("B")
                break
            else:
                # 벽이거나 다른 거면
                break

    else:  # 아닐 땐 뭐부터 해도 상관없음
        while True:
            ni, nj = bi + di, bj + dj
            if arr[ni][nj] == ".":
                arr[bi][bj] = "."
                bi, bj = ni, nj
                arr[bi][bj] = "B"
            elif arr[ni][nj] == "O":
                arr[bi][bj] = "."
                gd.append("B")
                break
            else:
                # 벽이거나 다른 거면
                break

        while True:
            ni, nj = ri + di, rj + dj
            if arr[ni][nj] == ".":
                arr[ri][rj] = "."
                ri, rj = ni, nj
                arr[ri][rj] = "R"
            elif arr[ni][nj] == "O":
                arr[ri][rj] = "."
                gd.append("R")
                break
            else:
                # 벽이거나 다른 거면
                break

    if "B" in gd:
        return ri, rj, bi, bj, -1

    # 위에 안 걸리고 여기에 걸린다는 건 A만 있다는 거니까
    elif "R" in gd:
        return ri, rj, bi, bj, 1

    else:
        return ri, rj, bi, bj, 0


def move_down(ri, rj, bi, bj):
    # 현재 구슬의 위치를 매개변수로 가져옴
    # 그렇다면 맵에도 동일하게 반영되어있음
    # 원상복귀할 때 맵에 바꿔주면 됨

    di, dj = 1,0
    good = 0
    gd = []

    if rj == bj and ri > bi:
        while True:
            ni, nj = ri + di, rj + dj
            if arr[ni][nj] == ".":
                arr[ri][rj] = "."
                ri, rj = ni, nj
                arr[ri][rj] = "R"
            elif arr[ni][nj] == "O":
                # 나중에 맵에서 돌려줄 때는 R이 없음
                # 그냥 두번 .으로 만드는 꼴이 되고, R만 원래 자리에 생기면 됨
                arr[ri][rj] = "."
                gd.append("R")
                break
            else:
                # 벽이거나 다른 거면
                break
        while True:
            ni, nj = bi + di, bj + dj
            if arr[ni][nj] == ".":
                arr[bi][bj] = "."
                bi, bj = ni, nj
                arr[bi][bj] = "B"
            elif arr[ni][nj] == "O":
                arr[bi][bj] = "."
                gd.append("B")
                break
            else:
                # 벽이거나 다른 거면
                break

    else:  # 아닐 땐 뭐부터 해도 상관없음
        while True:
            ni, nj = bi + di, bj + dj
            if arr[ni][nj] == ".":
                arr[bi][bj] = "."
                bi, bj = ni, nj
                arr[bi][bj] = "B"
            elif arr[ni][nj] == "O":
                arr[bi][bj] = "."
                gd.append("B")
                break
            else:
                # 벽이거나 다른 거면
                break

        while True:
            ni, nj = ri + di, rj + dj
            if arr[ni][nj] == ".":
                arr[ri][rj] = "."
                ri, rj = ni, nj
                arr[ri][rj] = "R"
            elif arr[ni][nj] == "O":
                arr[ri][rj] = "."
                gd.append("R")
                break
            else:
                # 벽이거나 다른 거면
                break

    if "B" in gd:
        return ri, rj, bi, bj, -1

    # 위에 안 걸리고 여기에 걸린다는 건 A만 있다는 거니까
    elif "R" in gd:
        return ri, rj, bi, bj, 1

    else:
        return ri, rj, bi, bj, 0

# 백트래킹 함수 ================================================
# 몇번 돌았는지, R 좌표, B 좌표, 성공했는지 flag
def btk(cnt, ri, rj, bi, bj, good):
    global ans

    if good == 1:
        ans = min(cnt, ans)
        return

    if good == -1:
        return

    if cnt == 10:
        return

    # 좌
    # 원래 구슬이 있는 좌표를 넘기고
    a, b, c, d = ri, rj, bi, bj
    # 돌려서 새로운 구슬의 좌표를 만들고
    ri, rj, bi, bj, good = move_left(a, b, c, d)
    # 여기서 맵도 바꿔짐
    btk(cnt + 1, ri, rj, bi, bj, good)
    arr[ri][rj] = "."
    arr[a][b] = "R"
    arr[bi][bj] = "."
    arr[c][d] = "B"
    # 원상복귀할 떄는 원래 구슬의 위치로
    ri, rj, bi, bj = a, b, c, d

    # 우
    a, b, c, d = ri, rj, bi, bj
    # 돌려서 새로운 구슬의 좌표를 만들고
    ri, rj, bi, bj, good = move_right(a, b, c, d)
    # 여기서 맵도 바꿔짐
    btk(cnt + 1, ri, rj, bi, bj, good)
    arr[ri][rj] = "."
    arr[a][b] = "R"
    arr[bi][bj] = "."
    arr[c][d] = "B"
    # 원상복귀할 떄는 원래 구슬의 위치로
    ri, rj, bi, bj = a, b, c, d

    # 상
    a, b, c, d = ri, rj, bi, bj
    # 돌려서 새로운 구슬의 좌표를 만들고
    ri, rj, bi, bj, good = move_up(a, b, c, d)
    # 여기서 맵도 바꿔짐
    btk(cnt + 1, ri, rj, bi, bj, good)
    arr[ri][rj] = "."
    arr[a][b] = "R"
    arr[bi][bj] = "."
    arr[c][d] = "B"
    # 원상복귀할 떄는 원래 구슬의 위치로
    ri, rj, bi, bj = a, b, c, d

    # 하
    a, b, c, d = ri, rj, bi, bj
    # 돌려서 새로운 구슬의 좌표를 만들고
    ri, rj, bi, bj, good = move_down(a, b, c, d)
    # 여기서 맵도 바꿔짐
    btk(cnt + 1, ri, rj, bi, bj, good)
    arr[ri][rj] = "."
    arr[a][b] = "R"
    arr[bi][bj] = "."
    arr[c][d] = "B"
    # 원상복귀할 떄는 원래 구슬의 위치로
    ri, rj, bi, bj = a, b, c, d


# main ============================================
N,M=map(int,input().split())
arr=[list(input()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == "R":
            ri,rj=i,j
        if arr[i][j] == "B":
            bi,bj=i,j

ans= 11
# 백트래킹 함수로 넘김 ===============================
btk(0,ri,rj,bi,bj,0)

if ans == 11:
    print(-1)
else:
    # 최종적으로는 ans 출력
    print(ans)