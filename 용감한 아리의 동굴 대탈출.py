'''
패딩이 필요하지 않았던 문제 !
[0] 사실 다 돌 필요가 없던게 꽉 찼다 -> 석순 없다니까
이걸 visited로 관리할 때 출발점 visited 안 해줬고, 다 같을 때를 패딩 전 수로 함

[1] bfs에서 visited 처리 안 해줬고 아래 코드도 빼먹음 근데 이거 전에도 빼먹었었음
if life == 1:
    return

[2] 사실 다 돌 필요가 없던게 꽉 찼다 -> 석순 없다니까

그리고 이 문제에서 헷갈릴만한 부분은 회전할때 아리 체력 무조건 주는 것
'''

def my_print():
    print('아리 위치와 방향,체력,공격력')
    print(ai, aj, ad, ari_life, ari_atk)
    print("===")
    print('보스 위치와 방향,체력,공격력')
    print(bi, bj, bd, boss_life, boss_atk)
    print("===")
    for row in arr:
        print(*row)
    print("===")


# N은 행, M은 열
N, M = map(int, input().split())

# 동굴
arr = [list(map(int, input().split())) for _ in range(N)]

# 상, 우, 하 , 좌 순서
dic = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

ari_life, ari_atk, boss_life, boss_atk = map(int, input().split())

suk = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            ai, aj = i, j
            arr[i][j] = 0

        if arr[i][j] == 1:
            suk.append((i, j))

for num in range(0, 4):
    di, dj = dic[num]
    ni, nj = ai + di, aj + dj
    if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 3:
        arr[ni][nj] = 0
        bi, bj = ni, nj
        bd = (num + 2) % 4
        ad = (num + 2) % 4

# my_print()
# =====================================

while True:

    # [1] 아리의 공격
    boss_life -= ari_atk

    if boss_life <= 0:
        print("VICTORY!")
        break

    # print('# [1] 아리의 공격 후')
    # my_print()

    # [2] 아리의 이동 -> 이동 안 했으면 ad 그대로 해야하고, 여기서도 체력 -1씩
    prev_ai, prev_aj = ai, aj
    prev_ad = ad

    for plus in range(0, 4):
        ad = (ad + plus) % 4
        di, dj = dic[ad]
        ni, nj = ai + di, aj + dj
        if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0 and (ni, nj) != (bi, bj):
            ai, aj = ni, nj
            ari_life -= plus
            break
    else:
        ad = prev_ad
        ari_life -= 4  # 회전하긴 했으니까

    if ari_life <= 0:
        print("CAVELIFE...")
        break


    # print('# [2] 아리의 이동 후')
    # my_print()
    # [3] 보스의 공격

    # 현재 보스의 방향에 따라서 달팽이로 돌면서 찾음
    # 단 보스의 위치가 가운데가 아닐 수 있으니 범위 넘어갈 수 있음
    # 모든 위치를 다 확인한 후에 끝
    def find_one(bi, bj, bd):

        if not suk:
            return -1, -1

        cnt = 1
        flag = False

        while True:
            for _ in range(2):
                for _ in range(cnt):
                    di, dj = dic[bd]
                    bi, bj = bi + di, bj + dj

                    if 0<=bi<N and 0<=bj<M and arr[bi][bj] == 1:
                        sec_i, sec_j = bi, bj
                        flag = True
                        break

                if flag:
                    break
                bd = (bd + 1) % 4

            if flag:
                break
            cnt += 1

        return sec_i, sec_j


    sec_i, sec_j = find_one(bi, bj, bd)
    # print('부하 위치',sec_i,sec_j)
    from collections import deque

    def bfs(sec_i, sec_j, ai, aj):
        global ari_life

        q = deque([(sec_i, sec_j, boss_atk)])
        v = [[0] * M for _ in range(N)]
        v[sec_i][sec_j] = 1

        while q:
            ci, cj, life = q.popleft()

            if (ci, cj) == (ai, aj) and life > 0:
                ari_life -= life
                return

            if life == 1:
                return

            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni, nj = ci + di, cj + dj
                if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0 and v[ni][nj]==0 and (ni, nj) != (bi, bj):
                    q.append((ni, nj, life - 1))
                    v[ni][nj] = 1

        return

    # (-1,-1)이 아니라면 부하가 생긴 것 !
    if (sec_i, sec_j) != (-1, -1):
        bfs(sec_i, sec_j, ai, aj)

    if ari_life <= 0:
        print("CAVELIFE...")
        break
    # print('# [3] 보스의 공격 후')
    # my_print()
    # 이동을 했으면 (prev_ai,prev_aj) != (ai,aj) 일거고 그렇다면 ad를 사용하면 되고
    # 만약 똑같다면 안 바꾸면 됨

    # [4] 보스의 이동
    if (prev_ai, prev_aj) != (ai, aj):
        bi, bj = prev_ai, prev_aj
        bd = ad

    # print('# [4] 보스의 이동 후')
    # my_print()