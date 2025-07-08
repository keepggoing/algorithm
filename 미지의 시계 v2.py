def myprint_3d(arr3):
    for arr in arr3:
        for lst in arr:
            print(*lst)
        print()
    print()


def myprint_2d(arr):
    for lst in arr:
        print(*lst)
    print()


def find_3d_start():
    for i in range(M):
        for j in range(M):
            if arr3[4][i][j] == 2:
                return 4, i, j


def find_2d_end():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 4:
                arr[i][j] = 0
                return i, j


def find_3d_base():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 3:
                return i, j


def find_3d_end_2d_start():
    # [1] 3차원 시작 좌표
    bi,bj=find_3d_base()

    # [2] 3차원 좌표에서 2차원 연결좌표 찾기
    for i in range(bi,bi+M):
        for j in range(bj,bj+M):
            

##########################################################

N, M, F = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 0 동, 1 서, 2 남, 3 북, 4 윗면 단면도
arr3 = [[list(map(int, input().split())) for _ in range(M)] for _ in range(5)]
wall = [list(map(int, input().split())) for _ in range(F)]

# [1] 주요 위치들 찾기
# 3차원 시작, 3차원 끝, 2차원 시작, 2차원 끝 좌표 탐색
sk_3d, si_3d, sj_3d = find_3d_start()
ei, ej = find_2d_end()
ek_3d, ei_3d, ej_3d, si, sj = find_3d_end_2d_start()
