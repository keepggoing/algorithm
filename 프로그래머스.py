# 시작 위치는 (0,0) 이고 (N-1,N-1)에 도착해야함
from collections import deque

# 0은 가로 모양, 1은 세로 모양
# 매초에 할 수 있는 일은 같은 방향으로 한 칸 이동,
# 혹은 축 둘 중 하나로 회전
board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]

def solution(board):
    N = len(board)
    # shape, 좌표
    v = [[[-1, -1] for _ in range(N)] for _ in range(N)]
    q = deque([(0, 0, 0)])
    v[0][0][0] = 0

    while q:
        shape, ci, cj = q.popleft()

        # 1. 종료 조건
        if v[N - 1][N - 2][0] != -1:
            for row in v:
                print(*row)
            return v[N - 1][N - 2][0]

        if v[N - 2][N - 1][1] != -1:
            return v[N - 2][N - 1][1]

        # 2. 현재 shape이 가로일때
        if shape == 0:
            # 2-1. 상하는 둘다 비어있어야 한다
            for di, dj in ((-1, 0), (1, 0)):
                ni,nj = ci + di, cj + dj

                # ni만 바뀌고, shape도 안 바뀌고,
                if 0 <= ni < N and v[ni][nj][shape] == -1 and board[ni][nj] == 0 and board[ni][nj+1] == 0:
                    q.append((shape, ni, nj))
                    v[ni][nj][shape] = v[ci][cj][shape] + 1

            # 2-2. 좌
            di, dj = 0, -1
            ni, nj = ci + di, cj + dj
            # 범위 내, 방문 안 했고, 모두 빈칸일 때
            if 0 <= nj < N and v[ni][nj][shape] == -1 and board[ni][nj] == 0:
                q.append((shape, ni, nj))
                v[ni][nj][shape] = v[ci][cj][shape] + 1

            # 2-3. 우
            di, dj = 0, 1
            ni, nj = ci + di, cj + dj
            # 범위 내, 방문 안 했고, 모두 빈칸일 때
            if 0 <= nj+1 < N and v[ni][nj][shape] == -1 and board[ni][nj+1] == 0:
                q.append((shape, ni, nj))
                v[ni][nj][shape] = v[ci][cj][shape] + 1

            # 2-4. 회전
            # ci,cj 고정
            if ci + 1 < N and v[ci][cj][1-shape] == -1 and board[ci + 1][cj] == 0 and board[ci + 1][cj + 1] == 0:
                q.append((1 - shape, ci, cj))
                v[ci][cj][1 - shape] = v[ci][cj][shape] + 1

            if ci - 1 < N and v[ci-1][cj][1-shape] == -1 and board[ci-1][cj] == 0 and board[ci-1][cj + 1] == 0:
                q.append((1 - shape, ci-1, cj))
                v[ci-1][cj][1 - shape] = v[ci][cj][shape] + 1

            # ci,cj+1을 pivot으로
            if ci + 1 < N and v[ci][cj + 1][1-shape] == -1 and board[ci + 1][cj] == 0 and board[ci + 1][cj+1] == 0:
                q.append((1 - shape, ci, cj + 1))
                v[ci][cj + 1][1 - shape] = v[ci][cj][shape] + 1

            if ci - 1 < N and v[ci-1][cj + 1][1-shape] == -1 and board[ci-1][cj] == 0 and board[ci-1][cj + 1] == 0:
                q.append((1 - shape, ci-1, cj + 1))
                v[ci-1][cj + 1][1 - shape] = v[ci][cj][shape] + 1

        # 세로일 때는
        else:
            # 좌우일 때는 모두 확인
            for di, dj in ((0, -1), (0, 1)):
                ni, nj = ci + di, cj + dj
                nni, nnj = ci + di + 1, cj + dj
                # 범위 내, 방문 안 했고, 모두 빈칸일 때
                if 0 <= ni < N and 0 <= nj < N and 0 <= nni < N and 0 <= nnj < N and v[ni][nj][shape] == -1 and \
                        board[ni][nj] == 0 and board[nni][nnj] == 0:
                    q.append((shape, ni, nj))
                    v[ni][nj][shape] = v[ci][cj][shape] + 1

            # 상으로 갈 때는
            di, dj = -1, 0
            ni, nj = ci + di, cj + dj
            # 범위 내, 방문 안 했고, 모두 빈칸일 때
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj][shape] == -1 and board[ni][nj] == 0:
                q.append((shape, ni, nj))
                v[ni][nj][shape] = v[ci][cj][shape] + 1

            # 하로 갈 때는
            di, dj = 1, 0
            ni, nj = ci + di + 1, cj + dj
            # 범위 내, 방문 안 했고, 모두 빈칸일 때
            if 0 <= ni < N and 0 <= nj < N and v[ni - 1][nj][shape] == -1 and board[ni][nj] == 0:
                q.append((shape, ni - 1, nj))
                v[ni - 1][nj][shape] = v[ci][cj][shape] + 1

            # 회전
            # ci,cj를 pivot으로
            if cj + 1 < N and v[ci][cj][1 - shape] == -1 and board[ci][cj + 1] == 0 and board[ci + 1][cj + 1] == 0:
                q.append((1 - shape, ci, cj))
                v[ci][cj][1 - shape] = v[ci][cj][shape] + 1

            if cj - 1 < N and v[ci][cj-1][1 - shape] == -1 and board[ci][cj-1] == 0 and board[ci + 1][cj - 1] == 0:
                q.append((1 - shape, ci, cj-1))
                v[ci][cj-1][1 - shape] = v[ci][cj][shape] + 1

            # ci,cj+1을 pivot으로
            if cj + 1 < N and v[ci + 1][cj][1 - shape] == -1 and board[ci][cj + 1] == 0 and board[ci + 1][cj + 1] == 0:
                q.append((1 - shape, ci + 1, cj))
                v[ci + 1][cj][1 - shape] = v[ci][cj][shape] + 1

            if cj - 1 < N and v[ci+1][cj-1][1 - shape] == -1 and board[ci][cj-1] == 0 and board[ci + 1][cj - 1] == 0:
                q.append((1 - shape, ci+1, cj-1))
                v[ci+1][cj-1][1 - shape] = v[ci][cj][shape] + 1


print(solution(board))
