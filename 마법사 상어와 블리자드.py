'''2차 풀이
[0] 타임라인
구상 (15분)
구현 (40분)
디버깅 (20분)

[1] 실수한 점
1. remove(0) 하면 모든 0이 지워지는 거 아님

2. 아래처럼 코드를 쓴다면 값이 다를 때만 처리를 해주기 때문에 마지막 pivot과 cnt는 반영이 안됨
-> 리스트를 앞에서 하나씩 비교할 때 마지막 값도 잘 처리되는지 확인하기

for i in range(1,len(lst)):
    if lst[i] == pivot:
        cnt+=1
    else:
        if cnt >= 4:
            flag=True
            score+=pivot*cnt
            for j in range(i-1,i-1-cnt,-1):
                lst[j]=0
        pivot=lst[i]
        cnt=1

3. len(lst)라고 써야하는데 아예 관계 없는 N이라고 씀
-> 마지막 검토할 때 모든 변수 하나하나 의미 생각하면서 잘 썼는지 검토하기

-> 2,3번 체크리스트 추가하기

[2] 배울점
1. 내 달팽이 코드에는 flag 2번 확인해야 최종적으로 나갈 수 있는 거 잊지말기
2. 리스트 앞에서 하나씩 볼 때 마지막에 변수에 남은 값 처리해줘야 하는 거 2048 에서도 주의해야할 부분이였음

'''

# 격자의 크기 N, 총 라운드 수 M
N,M=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]

# 우 하 좌 상
dic={0:(0,1),1:(1,0),2:(0,-1),3:(-1,0)}
si,sj=N//2,N//2
score=0


def flatten(arr):
    # 좌 하 우 상
    ddic={0:(0,-1),1:(1,0),2:(0,1),3:(-1,0)}
    lst=[]
    cnt=1
    flag=False
    si,sj=N//2,N//2
    d=0

    while True:
        for _ in range(2):
            di,dj=ddic[d]
            for _ in range(cnt):
                si,sj=si+di,sj+dj
                if arr[si][sj]!=0:
                    lst.append(arr[si][sj])
                if (si,sj)==(0,0):
                    flag=True
                    break
            d=(d+1)%4
            if flag:
                break
        if flag:
            break
        cnt+=1

    return lst

def again(lst):
    # 좌 하 우 상
    ddic={0:(0,-1),1:(1,0),2:(0,1),3:(-1,0)}
    arr=[[0]*N for _ in range(N)]
    idx=0
    cnt=1
    flag=False
    si,sj=N//2,N//2
    d=0

    while True:
        for _ in range(2):
            di,dj=ddic[d]
            for _ in range(cnt):
                si,sj=si+di,sj+dj
                arr[si][sj]=lst[idx]
                idx+=1
                if idx>=len(lst) or (si,sj)==(0,0):
                    flag=True
                    break
            d=(d+1)%4
            if flag:
                break
        if flag:
            break
        cnt+=1

    return arr

for _ in range(M):
    d,p=map(int,input().split())
    di,dj=dic[d]

    for mul in range(1,p+1):
        ni,nj=si+di*mul,sj+dj*mul
        if 0<=ni<N and 0<=nj<N and arr[ni][nj]!=0:
            score+=arr[ni][nj]
            arr[ni][nj]=0

    lst=flatten(arr)

    while True:
        if lst:
            pivot=lst[0]
            cnt=1
            flag=False
            for i in range(1,len(lst)):
                if lst[i] == pivot:
                    cnt+=1
                else:
                    if cnt >= 4:
                        flag=True
                        score+=pivot*cnt
                        for j in range(i-1,i-1-cnt,-1):
                            lst[j]=0
                    pivot=lst[i]
                    cnt=1
            if cnt>=4:
                score += pivot * cnt
                for j in range(len(lst)-1,len(lst)-1-cnt, -1):
                    lst[j] = 0

            if flag:
                new_lst=[]
                for i in range(len(lst)):
                    if lst[i] != 0:
                        new_lst.append(lst[i])
                lst=new_lst
            else:
                break
        else:
            break

    if lst:
        new_lst=[]
        pivot=lst[0]
        cnt=1
        for i in range(1,len(lst)):
            if lst[i]==pivot:
                cnt+=1
            else:
                new_lst.append(cnt)
                new_lst.append(pivot)
                pivot=lst[i]
                cnt=1
        new_lst.append(cnt)
        new_lst.append(pivot)

        arr=again(new_lst)
    else:
        break

print(score)

'''
B21611 마법사 상어와 블리자드/ 2025-03-20 / 체감 난이도 : 골드 1
소요 시간 : 1시간 50분 / 시도 : 3회 (인덱스 에러 2회)

[0] 총평
- 폭발을 해서 구슬이 아예 안 남는 경우가 있을 수 있는데 고려를 안함
엣지 케이스를 직접 만드는 건 아직 부족함

[1] 타임라인
1. 문제 이해 & 구상 (20분)
2. 구현 (50분)
3. 디버깅 (40분)

[2] 배운점 및 실수한 점
- 나는 모든 작업에서 달팽이를 돌렸는데 사실 2차원 배열을 1차원으로 변환해서 모든 작업을 하면 됨 !!!

[3] 시간 복잡도
50x50 2차원 배열을 빙글빙글
1최대 100번 하니까
25x10^4

[4] 엣지케이스
구슬이 아예 없을 수 있나? 처음엔 안 되겠지만 다 폭발해서 없는 상황이 만들어질 수 있음
제출 전에 이렇게 되나? 저렇게 되나? 좀 생각해봐야 함 !!!!!!

7 1
0 0 0 0 0 0 0
2 2 2 2 2 2 0
2 3 2 2 2 1 0
2 3 1 0 2 1 0
3 3 1 1 1 1 2
3 3 3 3 3 3 2
3 3 2 2 2 2 2
2 2

77
'''

def move():
    global arr

    temp = []

    di = [0, 1, 0, -1]
    dj = [-1, 0, 1, 0]

    i, j = N // 2, N // 2
    dr = 0
    dist = 1
    flag = False

    while True:
        if flag:
            break
        for _ in range(2):
            if flag:
                break
            for _ in range(dist):
                if (i, j) == (0, 0):                    # 내 달팽이에서는 이렇게 while문을 나감
                    flag = True
                    break
                i, j = i + di[dr], j + dj[dr]
                if arr[i][j] != 0:
                    temp.append(arr[i][j])             # 달팽이 돌면서 temp에 0이 아닌 숫자 다 넣음
            dr = (dr + 1) % 4
        dist += 1

    # idx는 temp의 인덱스로 숫자 하나씩 넣어줄 거고
    if len(temp)>0:
        new_arr = [[0] * N for _ in range(N)]         # new 배열에 또 달팽이 돌면서 숫자 다 넣음 ( 하나씩 당겨지는 거 해결 )
        i, j = N // 2, N // 2
        dr = 0
        dist = 1
        flag = False
        idx=0
        while True:
            if flag:
                break
            for _ in range(2):
                if flag:
                    break
                for _ in range(dist):
                    if (i, j) == (0, 0):
                        flag = True
                        break
                    i, j = i + di[dr], j + dj[dr]
                    new_arr[i][j] = temp[idx]
                    idx+=1

                    if idx==len(temp):              # 배열을 다 안 돌았지만 넣을 숫자가 끝났으면 나가 !
                        flag=True
                        break
                dr = (dr + 1) % 4
            dist += 1

        arr=[row[:] for row in new_arr]

def bomb():
    global a,b,c
    di = [0, 1, 0, -1]
    dj = [-1, 0, 1, 0]

    i, j = N // 2, N // 2
    dr = 0
    dist = 1
    flag = False
    keep = False        # 한 번이라도 폭발된 게 있으면 계속 해야함

    pivot,cnt=-1,0          # 기준 구슬 번호, 몇번 나왔는지

    # 좌표 담을 거
    tp=[]
    while True:
        if flag:
            break
        for _ in range(2):
            if flag:
                break
            for _ in range(dist):
                if (i, j) == (0, 0):
                    flag = True
                    break
                i, j = i + di[dr], j + dj[dr]
                if pivot != arr[i][j]:
                    if cnt >= 4:                    # 4번 이상 나왔을 때
                        keep=True                   # keep 플래그 바꿔주고
                        if pivot == 1:
                            a+=cnt
                        elif pivot == 2:
                            b+=cnt
                        elif pivot == 3:
                            c+=cnt
                        for x,y in tp:
                            arr[x][y]=0            # 0으로 바꾸기
                    tp=[(i,j)]
                    pivot=arr[i][j]
                    cnt=1
                else:
                    cnt+=1
                    tp.append((i,j))
            dr = (dr + 1) % 4
        dist += 1
    return keep

def change():
    global arr

    di = [0, 1, 0, -1]
    dj = [-1, 0, 1, 0]

    i, j = N // 2, N // 2
    dr = 0
    dist = 1
    flag = False
    pivot, cnt = -1, 0          # 기준 구슬 번호,몇번 나왔는지

    # tp에 ( 구슬의 개수, 구슬의 번호 ) extend로 펼쳐서 담을 거야
    tp = []
    while True:
        if flag:
            break
        for _ in range(2):
            if flag:
                break
            for _ in range(dist):
                if (i, j) == (0, 0):
                    flag = True
                    break
                i, j = i + di[dr], j + dj[dr]
                if pivot != arr[i][j]:
                    if cnt>0:
                        tp.extend((cnt,pivot))
                    pivot = arr[i][j]
                    cnt = 1
                else:
                    cnt += 1
            dr = (dr + 1) % 4
        dist += 1

    if len(tp)>0:
        new_arr = [[0] * N for _ in range(N)]
        i, j = N // 2, N // 2
        dr = 0
        dist = 1
        flag = False
        idx = 0
        while True:
            if flag:
                break
            for _ in range(2):
                if flag:
                    break
                for _ in range(dist):
                    if (i, j) == (0, 0):
                        flag = True
                        break
                    i, j = i + di[dr], j + dj[dr]
                    new_arr[i][j] = tp[idx]
                    idx += 1

                    if idx == len(tp):
                        flag = True
                        break
                dr = (dr + 1) % 4
            dist += 1

        arr = [row[:] for row in new_arr]


# NxN 격자, M은 블리자드 수행 횟수
N,M=map(int,input().split())

# 격자
arr=[list(map(int,input().split())) for _ in range(N)]
dic={1:(-1,0),2:(1,0),3:(0,-1),4:(0,1)}
si,sj=N//2,N//2
a,b,c=0,0,0

for _ in range(M):
    d,s=map(int,input().split())

    # [1] 빈칸으로 만들기
    di,dj=dic[d]
    for mul in range(1,s+1):
        ni,nj=si+di*mul,sj+dj*mul
        arr[ni][nj]=0

    # [2] 빈칸이 있으면 땡긴다
    move()

    # [3] 4개 이상 연속하는 구슬이 있을 때 폭발한다
    while True:
        keep=bomb()
        if not keep:
            break
        move()

    # [4] 구슬의 상태가 바뀐다
    change()

print(a+2*b+3*c)

