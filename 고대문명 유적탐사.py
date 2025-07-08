''' 2차풀이
[0] 타임라인
[1] 실수한점
1. 문제조건 누락 열,행 순으로 우선순위를 주어야 하는데 행,열 순으로 줌
2. i,j 오타 및 180도 회전,270도 회전 바꿔씀

'''
from collections import deque

# 탐사 반복 횟수 K, 벽면에 적힌 개수 M
K,M=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(5)]
wall=deque(map(int,input().split()))

def bfs(i,j,arr):
    q=deque([(i,j)])
    v[i][j]=1
    cnt=1
    temp=[(i,j)]

    while q:
        ci,cj=q.popleft()
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj=ci+di,cj+dj
            if 0<=ni<5 and 0<=nj<5 and arr[ci][cj]==arr[ni][nj] and v[ni][nj]==0:
                q.append((ni,nj))
                v[ni][nj]=1
                cnt+=1
                temp.append((ni,nj))

    if cnt>=3:
        lst.extend(temp)
    return

for _ in range(K):

    pivot=(30,360,5,5)

    for si in range(0,3):
        for sj in range(0,3):
            for rot in (90, 180, 270):
                new_arr = [row[:] for row in arr]
                for i in range(3):
                    for j in range(3):
                        if rot == 90:
                            new_arr[si+i][sj+j]=arr[si+2-j][sj+i]

                        elif rot == 180:
                            new_arr[si + i][sj + j] = arr[si + 2 - i][sj + 2 - j]

                        else:
                            new_arr[si + i][sj + j] = arr[si + j][sj + 2 - i]

                v=[[0]*5 for _ in range(5)]
                lst=[]
                for i in range(5):
                    for j in range(5):
                        if v[i][j]==0:
                            bfs(i,j,new_arr)

                if (-len(lst), rot, sj + 1, si + 1) < pivot:
                    pivot = (-len(lst), rot, sj + 1, si + 1)
                    final = new_arr                     # 이미 회전한 거
                    to_zero = lst                       # 없앨 수 있는 거

    #print(pivot)
    if pivot[0] == 0:                                   # 없앨 수 있는게 없으면 걍 끝내
        break

    lst=to_zero
    arr=final
    score=0

    while lst:
        score+=len(lst)

        for x,y in lst:
            arr[x][y]=0

        for j in range(5):
            for i in range(4,-1,-1):
                if arr[i][j]==0:
                    arr[i][j]=wall.popleft()

        lst = []
        v = [[0] * 5 for _ in range(5)]

        for i in range(5):
            for j in range(5):
                if v[i][j] == 0:
                    bfs(i, j,arr)

    print(score,end=" ")

'''
[체감 난이도 & 총평]
골 2

[시간복잡도]
K번 반복 10 x ( 27 번 돌고 각각마다 x value 함수 도는데 25 + M 최대 300 )

[타임라인]
0900 - 0914 구상
0916 - 0942 회전 & value 함수 구현 및 유닛테스트
0942 - 0957 나머지 구현
1002 - 1020 검증

[배운점 및 실수한 점]
- 회전하다가 당황한 점 : print를 for문 안에 두고 있어서 여러개 출력 됐는데 맨 처음꺼만 보고 왜 이상하게 회전되지? 생각하고 있었음
- 튜플 vs 튜플이 아니라 튜플  vs 숫자 비교를 하고 있었음 ** 튜플 vs 숫자 비교하면 오류 안 나고 그냥 다 다르다고 되니까 !!!!! 주의해야함
if pivot == 0:      # 더이상 할 게 없다면 끝낸다
    break
-> 체크리스트 추가하기

[추가 tc]
- 격자가 다 인접해 -> 우선순위 끝까지 확인 가능
2 25
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
3 2 3 5 2 4 6 1 3 2 5 6 2 1 5 6 7 1 2 3 2 3 4 5 6
ans : 25 6

'''

from collections import deque

def my_print():
    for row in arr:
        print(*row)
    print('------')

def value(temp):
    ans = 0
    v = [[0] * 5 for _ in range(5)]
    record=[]                       # 여기에는 비워야할 곳의 좌표가

    for i in range(5):
        for j in range(5):
            if v[i][j] == 0:
                q = deque([(i, j)])
                v[i][j] = 1
                val = 1
                lst=[(i,j)]

                while q:
                    ci, cj = q.popleft()
                    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        ni, nj = ci + di, cj + dj
                        if 0 <= ni < 5 and 0 <= nj < 5 and temp[ni][nj] == temp[i][j] and v[ni][nj] == 0:
                            q.append((ni, nj))
                            v[ni][nj] = 1
                            val += 1
                            lst.append((ni,nj))

                if val >= 3:            # 3이상이라면 record에 extend
                    ans += val
                    record.extend(lst)

    return ans, record

# =====================================================================================
# 반복횟수 K, 벽면에 적힌 유물 조각의 개수 M
K, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(5)]
wall = list(map(int, input().split()))


for _ in range(K):                                      # K번 반복할건데
    pivot = (0, 360, 6, 6)                              # 유물 1차 획득 가치를 최대화 - 회전 각도가 가장 작은 - 중심 좌표의 열이 작은 - 중심 좌표의 행이 작은
                                                        # pivot 보다 항상 작아야 한다
    for si in range(0, 3):
        for sj in range(0, 3):
            for rot in (90, 180, 270):                  # 세 각도 모두 회전해본다
                new_arr = [row[:] for row in arr]
                for i in range(3):
                    for j in range(3):
                        if rot == 90:
                            new_arr[si + i][sj + j] = arr[si + 2 - j][sj + i]
                        elif rot == 180:
                            new_arr[si + i][sj + j] = arr[si + 2 - i][sj + 2 - j]
                        else:
                            new_arr[si + i][sj + j] = arr[si + j][sj + 2 - i]

                ans, tp = value(new_arr)                # 1차 가치를 확인한다
                if (-ans, rot, sj+1, si+1) < pivot:
                    pivot=(-ans, rot, sj+1, si+1)
                    temp=[row[:] for row in new_arr]    # 회전한 결과도 temp에 복사해둔다

    # 끝나고 나면 temp에 회전된 거, pivot에 정보가 남는다
    # ==========================================================================
    if pivot[0] == 0:      # 더이상 할 게 없다면 끝낸다
        break
    # print(pivot)
    # ==========================================================================
    total=0
    arr = [row[:] for row in temp]  # 회전된 걸 arr로 반영 !

    while True:                     # 될 때까지 한다
        cnt,record=value(arr)
        if cnt == 0:                # 더이상 안 되면 멈춤
            break

        total+=cnt                  # 가치 더하고
        record.sort(key=lambda x:(x[1],-x[0]))      # 열 번호가 작고 - 행 번호가 큰 순서대로

        for i in range(len(record)):
            x,y=record[i]
            arr[x][y]=wall[i]                       # wall에 있는 수로 바꾸고
        wall=wall[len(record):]                     # wall 자른다
    #my_print()
    print(total, end=" ")


