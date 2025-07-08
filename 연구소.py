''' 2차 풀이
[체감난이도 & 총평]
골5

[타임라인]
0805-0810 구상
0810-0826 구현
0826- 0835 검증
-> 복붙 잘못해서 1회 오류

[시간복잡도]
조합 뽑기 120 x 그때마다 bfs 64x3번
맵이 작아서 ㄱㅊ

[추가 TC]
- 애초에 처음부터 빈칸이 없는 경우
3 4
1 1 2 1
2 2 2 1
2 2 2 1
ans:0
'''

from collections import deque

# n은 행, m은 열
n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]

# [1] 후보지 좌표 담기
can=[]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            can.append((i,j))

# 최소는 빈칸 없음
mx=0

# [3] 불 퍼지는 함수
def bfs(temp,new):
    q=deque()
    # 먼저 new에 있는 좌표들 벽으로 표시
    for i,j in new:
        temp[i][j]=1

    for i in range(n):
        for j in range(m):
            if arr[i][j]==2:                                # 여기만 arr임
                q.append((i,j))

    while q:
        ci,cj=q.popleft()
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj=ci+di,cj+dj
            if 0<=ni<n and 0<=nj<m and temp[ni][nj] == 0:
                temp[ni][nj]=2
                q.append((ni,nj))

    cnt=0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                cnt+=1

    return cnt

# [2] 백트래킹 함수로 3개 선택하기
def btk(cnt,idx,new):
    global mx

    if cnt == 3:
        # bfs 함수로 넘겨서 mx 구하기
        temp=[row[:] for row in arr]
        mx=max(mx,bfs(temp,new))
        return

    # 조합으로 뽑기
    for i in range(idx,len(can)):
        new.append((can[i]))
        btk(cnt+1,i+1,new)
        new.pop()

btk(0,0,[])

print(mx)

'''연구소 (1/58) / 2025-02-27 / 체감 난이도 : 골드 4-5
소요 시간 : 1시간 / 시도 : 1회 / 실행 시간 : 332ms / 메모리 : 134624KB

[타임라인]
1. 문제 이해 & 구상 & sudo code 작성 (15분)
2. 구현 (sudo code를 많이 적어놔서 거의 옮겨적기) (5분)
3. 디버깅 (30분)
4. 마지막 체크 (10분)

[디버깅 내역]
실수가 너무 많았다.......

1. from collections import deque 안 쓰고 popleft 하고 있었네

2. 백트래킹 종료조건 하나를 안 써서 인덱스 에러 났네 ( if idx==len(pos): return 요거 )
-> 이 두개를 끝냈는데 답이 이상하게 나와서 화장실 다녀와서 디버깅 시작

3. 답이 잘못 나옴
근거없이 bfs보다 백트래킹이 자신 없어서 (?) 백트래킹에서 문제 생겼을 거라고 생각함
- 1) 먼저 3개를 잘 찍고 있는 건지 확인함 (ok)
사실 뭘로 해도 똑같은데 부분집합 말고 조합으로 해야하나? 이게 틀렸나? 근거 없이 의심함 ..
그래서 조합으로 다시 dfs 함수를 짰는데 결과가 똑같이 잘못 나와서 문제는 bfs구나 깨달음
** 지금은 코드가 짧아서 괜찮았지만.. 앞으론 디버깅도 합리적 의심을 토대로 시작해야한다 !!!

- 2) 주어진 테케 말고 더 작은 테케로 돌리면서 temp와 arr을 모두 찍어봤는데, temp에서 바이러스가 확산이 안 되는 문제점을 발견함
q.append((ni,nj)) 이걸 안 해줬고, bfs 함수를 여러번 돌리는데 q를 딱 한번만 처음 넣어줘서 큐 관리가 제대로 안 된다는 사실을 발견함

[구상]
백트래킹 + bfs 느낌으로
0 인 곳 중에서 3개를 고르고, 그 3개를 1로 채운 후 bfs를 구해서 mx를 해보고를 반복해야겠다

[1] 먼저 돌면서 바꿀 수 있는 곳을 다 pos에 넣는다
[2] 백트래킹으로 가능한 거 다 하기
[3] bfs 함수로 정답 세기
바이러스가 있는 곳에서 다 시작해서 더이상 갈 곳이 없을 때까지 퍼뜨려야 함

[구현]


[마지막 체크 포인트]
마지막 테케가 한 3초 후에 결과가 나오길래 시간을 줄일 수 있는 방법을 고민함
그래서 고쳐보다가.. 별 차이가 없어서 좀 생각해봤는데 2초*3+2초 = 8초 넉넉해서 후에는 괜찮겠구나 생각함

[후기]
자잘한 실수를 너무 많이 했다 기본적인 것들 잘 챙기자
bfs랑 dfs는 어떻게 시간복잡도를 생각해야 하는지 모르겠어서 대충 했는데, 이거 팀원들에게 물어봐서 공부하자

'''

from collections import deque

# [3]
def bfs(new):
    # 깊은 복사 해줘야 한다
    temp = [row[:] for row in arr[:]]

    # 벽으로 바꿔주고
    for i, j in new:
        temp[i][j] = 1

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                q.append((i, j))

    # 가능할 때까지 바이러스 다 ~ 옮겨주기
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and temp[ni][nj] == 0:
                q.append((ni,nj))
                temp[ni][nj] = 2

    ans = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                ans += 1
    return ans

# [2]
def dfs(cnt,idx,new):
    global mx
    if cnt==3:
        # bfs(new)의 값은 new를 벽으로 다 바꾸고 나서 안전영역의 개수
        ans=bfs(new)
        mx=max(ans,mx)
        return

    if idx==len(pos):
        return

    # 선택했냐? 안했냐?
    # 여기가 좀 오래걸리는 것 같다
    dfs(cnt+1,idx+1,new+[pos[idx]])
    dfs(cnt,idx+1,new)

N,M=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
pos=[]
q=deque()
mx=0

for i in range(N):
    for j in range(M):
        if arr[i][j]==0:
            pos.append((i,j))

dfs(0,0,[])

print(mx)