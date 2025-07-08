from collections import deque

def solution(game_board, table):
    N = len(game_board)
    shape = []

    def bfs(si, sj):
        q = deque([(si, sj, 0, 0)])
        v[si][sj] = 1
        lst = []

        while q:
            ci, cj, dx, dy = q.popleft()
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni, nj = ci + di, cj + dj
                if 0 <= ni < N and 0 <= nj < N and table[ni][nj] == 1 and v[ni][nj] == 0:
                    q.append((ni, nj, dx + di, dy + dj))
                    v[ni][nj] = 1
                    lst.append((dx + di, dy + dj))
        shape.append(lst)

    v = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if v[i][j] == 0 and table[i][j] == 1:
                bfs(i, j)

    new_shape = [row[:] for row in shape]
    for sh in shape:
        lst1, lst2, lst3 = [], [], []
        for x, y in sh:
            lst1.append((y, -x))
            lst2.append((-x, -y))
            lst3.append((-y, x))
        new_shape.append(lst1)
        new_shape.append(lst2)
        new_shape.append(lst3)

    shape = new_shape

    ans = 0
    for i in range(N):
        for j in range(N):
            if game_board[i][j] == 0:
                for type in shape:
                    lst = [(i, j)]
                    for di, dj in type:
                        ni, nj = i + di, j + dj
                        if ni < 0 or ni >= N or nj < 0 or nj >= N or game_board[ni][nj] != 0:
                            break
                        lst.append((ni, nj))
                    else:
                        temp = [row[:] for row in game_board]
                        for x, y in lst:
                            temp[x][y] = 1
                        flag = False
                        for x, y in lst:
                            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                                ni, nj = x + di, y + dj
                                if 0 <= ni < N and 0 <= nj < N and temp[ni][nj] == 0:
                                    flag = True
                                    break
                            if flag:
                                break
                        else:
                            ans += len(lst)
                            game_board = temp
                            shape.remove(type)
                            lst1, lst2, lst3 = [], [], []
                            for x, y in type:
                                lst1.append((y, -x))
                                lst2.append((-x, -y))
                                lst3.append((-y, x))
                            shape.remove(lst1)
                            shape.remove(lst2)
                            shape.remove(lst3)
                            break
    return ans