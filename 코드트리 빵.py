'''
[체감 난이도 & 총평]
골 1
문제 이해가 잘 안 되고 헷갈렸다
그럴 때 적은 건 좋지만 충분한 고민으로 판단을 했는지? x, 근거를 찾고 결론을 냈다면 그 부분에 대한 찝찝합을 최대한 무시하고 짰는지? x
이것도 다 멘탈에 영향을 주는 거니까.. 최대한 논리적으로 판단하고 ( 예제에서 얻어낼 수 있는 건 최대한 얻어내기 )
확신이 섰다면 그때는 찝찝함을 최대한 무시하고 일단 짜기 -> 그리고 나중에 추가 검증

[시간복잡도]
n^2 + m마다 bfs n^2 + base마다 bfs n^2
225 + 20x225 + 195x225 = 1000000 10^6 정도 ok

[주의할 점]
- 격자에 있는 사람들 모두 한 칸만 움직일 건데 최단 거리로 움직인다?
-> 전체 경로가 최단 거리인데 한 칸만 가게 하겠다고? 근데 그 경로가 다음 턴에 막힐 수도 있지 않음? 그때 그때 구하라는 건가?

- 편의점에 도착한다면 격자에 있는 사람들이 모두 이동한 뒤 해당 칸 지나갈 수 없음
-> 모두 이동한 뒤 라는 건 1번 행동을 다 끝내고 나서지?

- t분이고 t<=m을 만족한다면 t번 사람이 베이스 캠프로 감
-> 처음에 잘못읽고 t번 사람만 움직이는게 아니라 모든 사람을 체크해줌 ( 어차피 t번 사람만 움직이게 되겠지만.. )

- 베이스 캠프를 못 쓴다는 건지 지나다닐 때만 못 쓴다는 건지..?
-> 예제를 보면 아예 못 쓰는 거로 되어있음

- 베이스 캠프 쓰고 나면 해당 턴 격자에 있는 사람들이 모두 이동한 뒤 지나갈 수 없다고 하는데.. 3단계니까 이미 격자에 있는 사람들은 다 움직인 거 아님?

[타임라인]
14:00 - 15:40 문제 잘못 이해 & 또 단계별 검증 안 하고 꼬임
# =========== 싹 지우고 다시 시작
15:40 - 16:00 근데도 문제 이해에 대한 확신이 없는데?
# =========== 5분간 휴식
16:05 - 16:25 구현
16:25 - 16:30 코드 검토 및 출력으로 확인

[배운점 및 실수한 점]
- tp=new.append((ni,nj)) 이런 요상한 문법을 사용하고 있..었음
append의 반환값이 없는데 ;;

[추가 TC]
- -1 처리 되어서 최단경로가 바뀌는 경우
5 2
0 0 0 0 0
0 0 0 0 0
0 1 0 0 0
0 0 0 0 0
0 0 0 0 1
5 2
5 1
'''

from collections import deque

# [3] 단계를 위한 bfs
def bfs(si,sj,x,y):
    q=deque([(si,sj,0)])
    v=[[0]*n for _ in range(n)]
    v[si][sj]=1

    while q:
        ci,cj,dist = q.popleft()

        if (ci,cj) == (x,y):
            return dist
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj=ci+di,cj+dj
            if 0<=ni<n and 0<=nj<n and arr[ni][nj] != -1 and v[ni][nj] == 0:
                q.append((ni,nj,dist+1))
                v[ni][nj]=1
    return -1

# [1] 단계를 위한 bfs
def bfs2(si,sj,ei,ej):
    q=deque([(si,sj,[])])                       # [] 에는 지금까지 사용한 방향을 담는다
    v=[[0]*n for _ in range(n)]
    v[si][sj]=1

    while q:
        ci,cj,new = q.popleft()
        if (ci,cj) == (ei,ej):
            return new                          # 경로에 가기 위해 사용한 방향을 return한다

        # 방향에 우선순위를 둔 채로 bfs를 돌렸으니까 처음 (ei,ej)에 도착하는 경로가 최적의 경로
        for di,dj in ((-1, 0), (0, -1), (0, 1),(1,0)):
            ni,nj=ci+di,cj+dj
            if 0<=ni<n and 0<=nj<n and arr[ni][nj] != -1 and v[ni][nj] == 0:
                tp=new+[(di,dj)]
                q.append((ni,nj,tp))
                v[ni][nj]=1
    return -1

# 격자의 크기와 사람의 수
n,m=map(int,input().split())

# 여기에 -1로 표시된 곳은 갈 수 없는 곳이다 !!!!
arr=[list(map(int,input().split())) for _ in range(n)]
base=[]

# 베이스 좌표가 쭉 들어가있다
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            base.append((i,j))

# 베캠에서 출발했는지, 편의점 도착 했는지, 가려고 하는 편의점 좌표, 현재 위치
p_loc=[[False, False,-1,-1,-1,-1] for _ in range(m+1)]

for i in range(1,m+1):
    x,y=map(int,input().split())
    x,y=x-1,y-1
    p_loc[i][2], p_loc[i][3]=x,y

time=0

while True:
    time+=1
    # [1] & [2] 가고 싶은 편의점 방향으로 1칸 간다
    no_con=[]
    for i in range(1,m+1):
        if p_loc[i][0] and not p_loc[i][1]:                                       # 베이스 캠프에서는 출발했고, 편의점에는 아직 도착하지 못한 경우
            new=bfs2(p_loc[i][4],p_loc[i][5],p_loc[i][2],p_loc[i][3])             # (si,sj,ei,ej) 즉, 현재 위치에서 편의점 위치로 가고 싶어
            di,dj=new[0]                                                          # 첫번째 있는게 당장 가야할 방향
            ni,nj=p_loc[i][4]+di,p_loc[i][5]+dj
            p_loc[i][4],p_loc[i][5]=ni,nj                                         # 위치 바꿔주고

            if (p_loc[i][4],p_loc[i][5]) == (p_loc[i][2],p_loc[i][3]) :           # 만약 편의점에 도착했으면
                p_loc[i][1]=True                                                  # 도착했다고 플래그 바꿔주고
                no_con.append((p_loc[i][4],p_loc[i][5]))                          # 한번에 못 가는 처리 해주기 위해서 일단 no_con에 담아

    for x,y in no_con:                                                            # 모든 사람 다 돌고나서 처리
        arr[x][y]=-1

    # =============================================================================
    # [3]
    no_base=[]
    if time<=m:
        si,sj = p_loc[time][2],p_loc[time][3]
        mx=225
        gi,gj=225,225

        for x,y in base:                                                          # 모든 베이스캠프에 대해서 bfs를 돌려본다
            dist=bfs(si,sj,x,y)
            if dist != -1:                                                        # 갈 수 있을 때
                if dist<mx:                                                       # 거리가 더 짧으면 mx,gi,gj 모두 바꿔주고
                    mx=dist
                    gi,gj=x,y
                elif dist==mx:                                                    # 거리가 같으면 튜플 ㅂ비교해서 gi,gj 바꿔주고
                    if (x, y) < (gi, gj):
                        gi, gj = x, y

        p_loc[time][0]=True                                                       # 베캠 도착했으니까 첫번째 플래그 바꿔주고
        p_loc[time][4],p_loc[time][5]=gi,gj                                       # 현재 위치 바꿔주고
        arr[gi][gj]=-1                                                            # 못 가는 곳으로 처리 !

    # [4] 모두 편의점에 도착했는지 확인 ! 만약 다 도착했으면 끝낸다
    for i in range(1, m + 1):
        if not p_loc[i][1]:                                                       # 두번째 플래그, 즉 편의점에 안 도착한게 있으면 break
            break
    else:
        print(time)                                                               # break 한 번도 안 했으면 끝 !
        break