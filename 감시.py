''' 2차 풀이 -> 3차 풀이 리스트에 추가
[타임라인]
1107 - 1114 구상
1114 - 1136 구현
1136 - 1144 디버깅
1144 - 1148 검증 -> 시간초과
1148 - 1210 디버깅 -> 너무 오래함

[시간복잡도]
자신의 말 8개에 대해서 4번 반복 가능 2**12

[실수한 점]
- 범위 밖 체크 안 해줘서 오픈테케 인덱스 에러
- for mul in range(1,8) 을 range 빼먹어서 1이랑 8만 확인
- 백트래킹할 때 자꾸 i+1로 해야하는데 idx+1로 쓰는 실수를 함
for i in range(idx, len(check)):
    ...
    btk(idx+1,arr) -> btk(i+1,arr)
-> 체크리스트에 추가하기

[추가 tc]
-처음부터 빈 곳이 없는 경우
4 4
6 6 6 6
6 2 6 6
6 6 6 5
6 1 6 6
ans:0
'''

# 행은 n, 열은 m
n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
check=[]

# 상 우 하 좌 순서대로
dic={0:(-1,0), 1:(0,1), 2:(1,0), 3:(0,-1)}
mal={1:[(0,),(1,),(2,),(3,)], 2:[(1,3),(0,2)], 3:[(0,1),(1,2),(2,3),(3,0)], 4:[(0,1,2),(1,2,3),(2,3,0),(3,0,1)], 5:[(0,1,2,3)]}

for i in range(n):
    for j in range(m):
        if 1<=arr[i][j]<=5:
            check.append((i,j))
mn=64

def btk(idx,arr):
    global mn

    if idx == len(check):
        ans=0
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:
                    ans+=1
        mn=min(ans,mn)
        return

    for i in range(idx, len(check)):
        si,sj=check[i]

        for direction in mal[arr[si][sj]]:
            # 여기서 복사
            tp=[row[:] for row in arr]
            for num in direction:
                di,dj=dic[num]
                for mul in range (1,8):
                    ni,nj=si+di*mul, sj+dj*mul
                    if ni<0 or ni>=n or nj<0 or nj>=m or arr[ni][nj]==6:
                        break
                    elif arr[ni][nj]==0:
                        arr[ni][nj]=9
                    else:
                        continue
            btk(i+1,arr)
            arr=[row[:] for row in tp]

btk(0,arr)
print(mn)

'''
### 코드 리뷰 ###

B15683 감시 / 2025-03-05 / 체감 난이도 : 골드 3
소요 시간 : 4시간 / 시도 : 3회 (틀렸습니다 -> 메모리 초과 -> 성공)

[0] 총평
- 처음 든 생각은 " 하 백트래킹 자신 없는데 .. "
백트래킹 코드를 못 짜겠어서 피하고 피했는데 날 기다리고 있었던 건 메모리 초과와 시간 초과
못 짜겠다고 시도 더 안 해보고 비효율적인 방법으로 틀면 .. 어차피 시간낭비다 쫄지말고 마주하자 !!!
백트래킹 코드 못 짤 것도 없음

[1] 타임라인
- 문제 이해 및 구상 (22분)
- 구현 (20분) -> 백트래킹에서 막힘
- 백트래킹 구현 고민 (40분) -> 포기하고 itertools 씀
- 구현 (20분)

-> 틀렸습니다 ~

[2] 배운점 및 실수한점

- 첫번째 코드가 틀린 이유 : 여러 cctv를 다 해보면서 cctv가 닿는 곳이면 +1 했는데, 이미 처리한 곳 표시를 안 해줌
- 두번째 코드가 메모리 초과난 이유 : 백트래킹 못 짜겠어서 가능한 모든 (좌표,방향)을 한 배열에 다 넣어줬음, 그리고 한 번에 같은 좌표를 두번 보면 그건 사용 안 한다 (중복체크 따로)
이렇게 짰는데, 가능한 모든 경우를 조합하니까 최악은 8개*4방향 C 8개 -> 10518300 여서 메모리 초과 + 시간 초과
_____

- cctv 1은 (0,1,2,3) 이고 cctv 2는 ((1,2),(2,3)) 이여서 int랑 튜플 오류남
-> 튜플 1개일 때는 (1,) 이렇게 해주면 됨

- 지금까지 백트래킹을 할 때에는 한 풀에서 조합을 만들었음, 하지만 이번에는 cctv가 1일때는 ~ 풀에서 뽑고, 2일 때는 ~ 풀에서 뽑고 .. 각각 풀이 다를 때 어떻게 해야할지 모름
-> 아래 NM 문제에서도 보면 range 뒤에 내가 뽑을 풀을 넣어주는 거자나 ?! <= 이게 포인트
for i in range(1,N+1):
    dfs(n+1,new+[i])

따라서 이렇게 어떤 cctv냐에 따라서 뒤에 풀을 달리하면 됨
def btk(cnt,command):
    if cnt == len(need_to_see):
        find_max(command)
        return

    for dr in match[need_to_see[cnt][0]]:
        command.append((need_to_see[cnt][1],need_to_see[cnt][2],dr))
        btk(cnt+1,command)
        command.pop()

- 중복 체크 함수 만들 때 i+1로 해야하는데 i로 썼음
for i in range(0,N):
    for j in range(i,N)

[3] 개선사항 (추가 예정)

'''
# 이건 5일 때만 돌린다
def fill(i,j,dr):
    for mul in range(1,max(N,M)):
        ni,nj=i+di[dr]*mul,j+dj[dr]*mul

        if ni<0 or N<=ni or nj<0 or M<=nj or arr[ni][nj]==6:
            return
        elif arr[ni][nj]==0:
            # 이거로 채워
            arr[ni][nj]='#'
        else:
            continue

def check(i,j,dr,v):
    cnt=0
    for mul in range(1,max(N,M)):
        ni,nj=i+di[dr]*mul,j+dj[dr]*mul
        # 범위 밖으로 나가면, 그리고 6이면 멈춰
        # 1~5 이면 그 수를 넘어서 다음으로 가면 되고
        # 0이면 채워
        if ni<0 or N<=ni or nj<0 or M<=nj or arr[ni][nj]==6:
            return cnt
        elif arr[ni][nj]==0 and v[ni][nj]==0:
            v[ni][nj]=1
            # 이거로 채워
            cnt+=1
        # 5나 # 모두 continue
        else:
            continue
    return cnt

def find_max(command):
    global mx
    # 여기서 하나씩 해보고 mx 값 구하기
    T = 0
    v = [[0] * M for _ in range(N)]
    for i in range(0, len(command)):
        if len(command[i][2]) == 1:
            T += check(command[i][0], command[i][1], command[i][2][0],v)
        else:
            for dr in command[i][2]:
                T += check(command[i][0], command[i][1], dr,v)
    mx = max(T, mx)

# cnt가 인덱스=몇개골랏냐, 완성된거지금까지
def btk(cnt,command):
    if cnt == len(need_to_see):
        find_max(command)
        return

    for dr in match[need_to_see[cnt][0]]:
        btk(cnt+1,command+[(need_to_see[cnt][1],need_to_see[cnt][2],dr)])


# 상우하좌
di=[-1,0,1,0]
dj=[0,1,0,-1]

N,M=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
need_to_see=[]

# 일단 5인 건 다 깔고 간다
for i in range(N):
    for j in range(M):
        if arr[i][j] == 5:
            for k in range(4):
                dr=k
                fill(i,j,dr)

        elif arr[i][j] == 1 :
            need_to_see.append((1,i,j))

        elif arr[i][j] == 2 :
            need_to_see.append((2,i,j))

        elif arr[i][j] == 3 :
            need_to_see.append((3,i,j))

        elif arr[i][j] == 4 :
            need_to_see.append((4,i,j))


mx=0
match={1:[(0,),(1,),(2,),(3,)],2:[(0,2),(1,3)],3:[(0,1),(1,2),(2,3),(3,0)],4:[(0,1,2),(1,2,3),(2,3,0),(3,0,1)]}
btk(0,[])

square=0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            square+=1

print(square-mx)
'''
내 코드 리팩토링
어떤게 나올 때까지 쭉 가고 싶을 때 while문으로 간단하게 처리, 
visited 배열로 cctv가 닿는 곳 체크해주면서 if arr[i][j]==0 and v[i][j]==0: 사각지대 간단하게 카운팅 

# =================================================
def find_min(command):
    v=[[0]*M for _ in range(N)]
    for i in range(len(need_to_see)):
        x,y,com=command[i]
        for dr in com:
            ci,cj=x,y
            while True:
                ci,cj=ci+di[dr],cj+dj[dr]
                if ci<0 or ci>=N or cj<0 or cj>=M or arr[ci][cj]==6:
                    break
                v[ci][cj]=1

    cnt=0
    for i in range(N):
        for j in range(M):
            if arr[i][j]==0 and v[i][j]==0:
                cnt+=1
    return cnt


# cnt가 인덱스=몇개골랏냐, 완성된거지금까지
def btk(cnt,command):
    global mn
    if cnt == len(need_to_see):
        mn=min(mn,find_min(command))
        return

    for dr in match[need_to_see[cnt][0]]:
        command.append((need_to_see[cnt][1],need_to_see[cnt][2],dr))
        btk(cnt+1,command)
        command.pop()

# 상우하좌
di=[-1,0,1,0]
dj=[0,1,0,-1]

N,M=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
need_to_see=[]

for i in range(N):
    for j in range(M):
        if 1<=arr[i][j]<= 5:
            need_to_see.append((arr[i][j],i,j))

mn=N*M
match={1:[(0,),(1,),(2,),(3,)],2:[(0,2),(1,3)],3:[(0,1),(1,2),(2,3),(3,0)],4:[(0,1,2),(1,2,3),(2,3,0),(3,0,1)],5:[(0,1,2,3)]}

btk(0,[])
print(mn)
'''