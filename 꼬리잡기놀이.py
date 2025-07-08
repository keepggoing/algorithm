'''
[체감 난이도 & 총평]
골 1
남은 시간 동안 내가 연습해야할 건 테케 틀리기 전에 생각하기 !!!
주의할 점 적고 검증, 테케 만들고 검증 안 하고 제출하면 진짜 ;

[시간 복잡도]
전처리 n**2 20x20
라운드 수 1000 돌면서 (m+m+n) 즉 (5+5+20) 정도 가능
ㄱㅊ

[주의할 점] -> 둘다 고려하지 못함 ;;
- 한 팀에 사람이 꽉 차있을 수 있다
- 아무도 공에 안 맞을 수 있다

[타임라인]
0915 문제이해 및 구상 완료
0940 절반 구현 완료 -> 공 던지기 구현하려고 하니까 구상 잘못 되었음을 느낌 (팀에서 몇번째인지, 공 맞은 사람은 몇번째 팀에 속하는지 관리가 쉽지 않음)
0950 재구상 완료 -> 맵에 (팀, 내가 팀에서 몇 번째인지) 로 기록하고 후보지는 4가 아니라 -1로
1014 구현 완료 및 제출 -> 틀렸습니다 ( 꽉차있는 경우 고려 x )
1035 2차 제출 -> 틀렸습니다 ( 꽉차있는 경우 고려 x )
1048 3차 제출 -> 틀렸습니다 ( 아무도 공을 안 맞는 경우 고려 x )

[배운점 및 실수한점]
- 덱은 [::-1] 안됨 -> 잠깐 리스트로 바꿔주면 됨
- 한 팀에 꽉 차있을 수 있는 경우 고려 못해서 고침 -> 또 틀림
같은 경우에 대해서 전처리할 때도 고쳐야했음 -> 하나 놓친 부분 있으면 그 부분에 관련해서 코드 다 검토 해야한다고 ..

[추가 TC]
- 꽉찬 경우
7 2 1
2 2 1 0 0 0 0
2 0 3 0 2 1 3
2 2 2 0 2 0 2
0 0 0 0 2 0 2
0 0 2 2 2 0 2
0 0 2 0 0 0 2
0 0 2 2 2 2 2

ans : 16

- 아무도 공에 안 맞는 경우
7 1 1
0 0 0 0 0 0 0
0 0 0 0 2 1 4
0 0 0 0 2 0 4
0 0 0 0 2 3 4
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0

ans:0
'''

from collections import deque

n,m,k=map(int,input().split())                          # 격자의 크기, 팀의 개수, 라운드 수
arr=[list(map(int,input().split())) for _ in range(n)]

team_loc=[deque() for _ in range(m)]                    # 팀 별로 머리부터 꼬리까지 순서대로 들어감 ( 각각은 덱 )

idx=-1
v=[[0]*n for _ in range(n)]

                                                        # arr 맵에는 (팀, 내가 팀에서 몇 번째인지) 로 들어감
for i in range(n):
    for j in range(n):
        if arr[i][j] == 4:
            arr[i][j] = -1                              # 4, 즉 갈 수 있는 후보지는 다 -1로
        if arr[i][j] == 1:
            v[i][j]=1                                   # 처음 꼬리인 곳을 만나면
            idx+=1                                      # idx번째 팀으로 만들고
            team_loc[idx].append((i,j))                 # team_loc[idx]에 하나씩 추가할 거임
            si,sj=i,j

            while True:
                for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                    ni,nj=si+di,sj+dj
                    if 0<=ni<n and 0<=nj<n and arr[ni][nj] != 4 and arr[ni][nj] != -1 and arr[ni][nj] != 0 and v[ni][nj] == 0:          # 범위 안이고 후보지 아니고 빈 곳 아니고 방문 안 했으면
                        if (si,sj) == (i,j) and arr[ni][nj]==3:             # 꽉차있을 때 3으로 먼저 가는 경우가 생길 수 있으니 이 조건문 필요 !!!
                            continue
                        v[ni][nj]=1                                         # 방문 표시 하고
                        team_loc[idx].append((ni,nj))                       # team_loc[idx]에 추가하고
                        si,sj=ni,nj                                         # 시작 지점으로 만들고 다시 돌아야함
                        break
                else:                                                       # 사방탐색해서 더이상 갈 수 없을 때까지
                    break

# ===============================================================
# 공이 날라오는 순서대로 1차원 배열에 넣을거임
ball=[]
for i in range(n):                              # 왼쪽에서 부터 봐라
    ball.append((0,i))

for i in range(n):                              # 밑에서부터 봐라
    ball.append((1,i))

for i in range(n-1,-1,-1):                       # 오른쪽에서부터 봐라
    ball.append((2,i))

for i in range(n-1,-1,-1):                       # 위에서부터 봐라
    ball.append((3,i))

# ===============================================================
ans=0

for turn in range(k):
    # [1] 각 팀은 머리사람을 따라서 한 칸 이동한다
    for i in range(m):
        fi,fj=team_loc[i][0]
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = fi + di, fj + dj
            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == -1:       # 시작 지점에서 갈 수 있는 후보지가 있다면
                team_loc[i].appendleft((ni,nj))                         # 시작 지점을 그곳으로 바꿔주고
                ei,ej=team_loc[i].pop()                                 # 맨 끝에 지점이였던 거만 빼주고
                arr[ei][ej]=-1                                          # arr에 반영 ( 나머지는 이따가 arr에 반영시킬거임 )
                break
        else:                                                           # 이 부분 누락했었음 !!!
            team_loc[i].rotate(1)                                       # 다 막혀있다면 시계방향 rotate해준다

                                                                        # 여기서 맵에 반영해준다
    for i in range(m):
        arr[team_loc[i][0][0]][team_loc[i][0][1]]=(i,1)                 # 머리는 1로
        arr[team_loc[i][-1][0]][team_loc[i][-1][1]] = (i, len(team_loc[i])) # 꼬리는 길이로
        for j in range(1,len(team_loc[i])-1):                           # 나머지는 각각 인덱스+1로
            arr[team_loc[i][j][0]][team_loc[i][j][1]]=(i,j+1)

# ===============================================================
    com=turn%len(ball)                                                   # 공 던지기
    command=ball[com]
    team=-1
    if command[0] == 0:                                                  # 방향에 따라 분기 처리
        for j in range(0,n):
            if arr[command[1]][j] != -1 and arr[command[1]][j] != 0:
                team,num=arr[command[1]][j]
                ans+=num**2
                team_loc[team]=deque(list(team_loc[team])[::-1])         # 잠시 리스트로 바꾸고 위치 반대로
                break

    elif command[0] == 1:
        for i in range(n-1,-1,-1):
            if arr[i][command[1]] != -1 and arr[i][command[1]] != 0:
                team, num = arr[i][command[1]]
                ans += num ** 2
                team_loc[team]=deque(list(team_loc[team])[::-1])
                break

    elif command[0] == 2:
        for j in range(n-1,-1,-1):
            if arr[command[1]][j] != -1 and arr[command[1]][j] != 0:
                team, num = arr[command[1]][j]
                ans += num ** 2
                team_loc[team]=deque(list(team_loc[team])[::-1])
                break

    elif command[0] == 3:
        for i in range(0,n):
            if arr[i][command[1]] != -1 and arr[i][command[1]] != 0:
                team, num = arr[i][command[1]]
                ans += num ** 2
                team_loc[team]=deque(list(team_loc[team])[::-1])
                break

    idx=1                                                         # team에는 방향 바꾼 팀 번호 있을 거니까
    if team != -1:                                                # 이 조건 누락했었음 !!! 안 맞은 팀 있을 수 있잖아
        for x,y in team_loc[team]:
            arr[x][y]=(team,idx)                                  # 맵에 바뀐 방향으로 다시 저장
            idx+=1

print(ans)
