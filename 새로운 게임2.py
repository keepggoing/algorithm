'''
- 각각의 인덱스를 가지고 다니면서 다닐 수 있음
- 그리고 파란색일 때 두번 볼 필요가 없음
'''

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

change={0:1,1:0,2:3,3:2}
# mal 배열에는 몇번째 말인지, 방향만 담고
mal = [[[] for _ in range(N)] for _ in range(N)]

# mal_loc에는 위치만 담는다
mal_loc = []
for i in range(K):
    x, y, d = map(int, input().split())
    # 행과 열은 1부터 시작
    x, y, d = x - 1, y - 1, d - 1
    mal[x][y].append((i, d))
    mal_loc.append((x, y))

turn = 1
while turn <= 1000:
    # 매 턴마다 모든 말이 움직인다
    for i in range(K):
        si, sj = mal_loc[i]
        for k in range(len(mal[si][sj])):
            num, d = mal[si][sj][k]
            if num == i:
                break
        ni, nj = si + di[d], sj + dj[d]
        # 파란색? 이거나 범위 밖
        if ni < 0 or ni >= N or nj < 0 or nj >= N or arr[ni][nj] == 2:
            d=change[d]

            ni, nj = si + di[d], sj + dj[d]
            if ni < 0 or ni >= N or nj < 0 or nj >= N or arr[ni][nj] == 2:
                # 새로 바뀐 방향으로만 바꿔치기
                mal[si][sj][k] = (i, d)

        # 흰색?
        if arr[ni][nj] == 0:
            for index, direction in mal[si][sj][k:]:
                mal_loc[index] = (ni, nj)
            for temp in mal[si][sj][k:]:
                mal[ni][nj].append(temp)
            mal[si][sj] = mal[si][sj][:k]

        # 빨간색?
        elif arr[ni][nj] == 1:
            for index, direction in mal[si][sj][k:]:
                mal_loc[index] = (ni, nj)
            for temp in mal[si][sj][k:][::-1]:
                mal[ni][nj].append(temp)
            mal[si][sj] = mal[si][sj][:k]

        # 한 곳에 4개인게 있으면 종료하고 그때의 turn을 출력한다
        flag = False
        for i in range(N):
            for j in range(N):
                if len(mal[i][j]) >= 4:
                    flag = True
                    break
            if flag:
                break
        if flag:
            print(turn)
            break
    if flag:
        break
    turn += 1
else:
    print(-1)