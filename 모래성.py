from collections import deque
# N 행, M열 ( 직사각형 )
N,M=map(int,input().split())

# 모래성의 상태 1~9는 모래의 강도, .은 모래가 없다는 뜻
# 격자의 가장자리에는 무조건 .
arr=[list(input()) for _ in range(N)]
q=deque()

def check(i,j):
    pivot = int(arr[i][j])
    cnt = 0
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)):
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == '.':
            cnt += 1
    if cnt >= pivot:
        q.append((i,j))
        return 1
    return 0

for i in range(N):
    for j in range(M):
        if arr[i][j] != '.' and int(arr[i][j]) != 9:
            check(i,j)

for x,y in q:
    arr[x][y]='.'

if not q: ans = 0
else: ans = 1

print(q)
# 큐에는 새롭게 . 이 된 좌표들이 들어가있고
while q:
    # 동시진행
    for _ in range(len(q)):
        ci,cj=q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != '.' and int(arr[ni][nj]) != 9:
                if check(ni,nj): q.append((ni,nj))

    for x,y in q:
        arr[x][y]='.'
    ans+=1

print(ans)

# 8방향을 봐서 모래성이 쌓여있지 않은 개수 >= 모래성의 튼튼함 : 파도에 의해서 무너질 수 있음
# 그 이외의 경우는 파도가 쳐도 무너지지 않음
# 모래성이 무너진 경우, 모래성이 쌓여있지 않은 것으로 취급
# 결국 한가지 형태로 수렴할 것

# 파도가 한번 칠때마다 특정부분이 무너져 내림
# 더이상 모래성의 모양이 변하지 않게 되려면 파도가 몇번 쳐야할까?

# 출력
# 몇번의 파도가 몰려오고 나서야 모래성의 상태가 수렴하는지?