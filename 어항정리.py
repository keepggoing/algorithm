'''
B23291 어항정리 / 2025-03-20 / 체감 난이도 : 플레 5 ~ 골드 1
소요 시간 : 3시간 / 시도 : 1회

[0] 총평
- 실수 넘 많았고 그래서 디버깅 시간이 넘 길었음
- 인덱스 계산할게 많았는데 이걸 그냥 머리로 한게 원인
종이에 쓰면서 했으면 실수가 덜 나왔을 텐데 !!!!
- 그것보다 NxN으로 안 들고 다녀도 됨 ! 길이가 다른 2차원 배열도 가능하거둔

[1] 타임라인
1. 문제 이해 & 구상 (20분)
2. 구현 (1시간 10분)
3. 디버깅 (1시간..)

[2] 배운점 및 실수한 점
- 그냥 천천히 위에서부터 로직 검토했으면 되는데 .. 숫자가 비슷하게 나오는 건 아무 의미없다
너무 여기봤다 저기봤다 했음

< 실수한 부분 >
1. 한 줄로 만드는 함수에서 숫자인 부분 쭉 붙이고 남은 부분은 0으로 채워줘야 하는데 안함
2. 공중부양해서 붙이고 나서 원래 있던 자리들은 0으로 바꿔야 하는데 그걸 안함
3. j>N-end 일 때 끝내야 하는데 j>N-1-end로 함
이런 건 무조건 손으로 쓰면서 해봤어야함
근데 또 마음 급해져서 막 바꿔봤지? 그러면 안 된다니까....
4. N//2로 두번 돌릴 때 일반화해서 안 적고 예시 숫자를 걍 넣어버림

-> 아무튼 꼼꼼함이 부족했던 것 !!!!!
이 문제는 찍어보면서 풀어야한다고 생각했기 때문에 손구상을 덜 했는데
찍어보면서도 일반화하면서 코드를 써야할 땐 종이에 해보면서 꼼꼼하게 했어야지 !

[3] 시간 복잡도
100x100 배열을 계속해서 10번 정도의 작업으로 계속 하니까
10^5 x 상수번

'''

def control_count():
    global arr
    new_arr = [row[:] for row in arr]

    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0:
                di, dj = 1, 0
                if 0 <= i + di < N and 0 <= j + dj < N and arr[i + di][j + dj] > 0:
                    # 둘다 0 이상이면
                    d = (abs(arr[i + di][j + dj] - arr[i][j])) // 5
                    if d > 0:
                        if arr[i][j] > arr[i + di][j + dj]:
                            new_arr[i][j] -= d
                            new_arr[i + di][j + dj] += d
                        else:
                            new_arr[i][j] += d
                            new_arr[i + di][j + dj] -= d
                di, dj = 0, 1
                if 0 <= i + di < N and 0 <= j + dj < N and arr[i + di][j + dj] > 0:
                    # 둘다 0 이상이면
                    d = (abs(arr[i + di][j + dj] - arr[i][j])) // 5
                    if d > 0:
                        if arr[i][j] > arr[i + di][j + dj]:
                            new_arr[i][j] -= d
                            new_arr[i + di][j + dj] += d
                        else:
                            new_arr[i][j] += d
                            new_arr[i + di][j + dj] -= d

    arr = [row[:] for row in new_arr]

# =========================================

def one_line():
    global arr
    new_arr = [[0] * N for _ in range(N)]
    temp = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                temp.append(arr[i][j])
    for _ in range(N-len(temp)):
        temp.append(0)
    new_arr[0] = temp
    new_arr = list(map(list, zip(*new_arr)))
    arr=[row[:] for row in new_arr]

# ============================================

# 어항의 수, 차이가 K 이하가 되도록 하고싶어
N,K=map(int,input().split())
arr=[[0]*N for _ in range(N)]       # 꽉찬 2차원 배열을 갖고 다님

lst=list(map(int,input().split()))
arr[N-1]=lst                        # 마지막 행에 넣고 시작 ( 아직 전치행렬 아님 )
ans=0

# ============================================
while True:
    # [0] 정답 확인 ( 0도 들어있기 이렇게 최대, 최소를 확인함 )
    mx=-1
    mn=10000

    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                mx=max(mx, arr[i][j])
                mn=min(mn, arr[i][j])
    if mx-mn<=K:
        print(ans)
        break
    ans+=1

    # ==========================================
    # [1] 가장 적은 어항에 넣는다 ( 전치행렬 아님 )

    for j in range(N):
        if arr[N-1][j] == mn:
            arr[N-1][j] +=1

    # =========================================
    # [2] 맨 왼쪽 어항을 하나 오른쪽에 올린다  ( 시계 방향 90도 회전해서 행으로 보기 시작 )
    arr[N-2][1]=arr[N-1][0]
    arr[N-1][0]=0
    arr=[row[:] for row in list(map(list,zip(*arr[::-1])))]

    # =========================================
    # [3] 90도 회전해서 쌓는 거 될 때까지 반복한다
    while True:
        for i in range(N):
            if arr[i][0] != 0:
                start=i             # start : 비어있지 않은 첫번째 행 인덱스
                break

        end=start+1                 # end : 돌려야 하는 마지막 행 인덱스 +1
        for i in range(start+1,N):
            # 0의 개수가 N-2 이하인 거 == 어항이 2개 이상이다
            if arr[i].count(0)<=N-2:
                end=i+1
            else:
                break

        j=arr[start].index(0)       # j : 0이 처음 나오는 인덱스 == 한 행에 어항 개수

        if j > N-end:               # 회전 시켜야 하는 어항 개수가 남은 행보다 크면 못 돌린다
            break

        temp=[row[:j] for row in arr[start:end]]    # temp에는 회전싴켜야 하는 사각형
        temp=list(map(list,zip(*temp[::-1])))       # 90도 회전시키고

        idx=0                                       # 회전시킨 건 end부터 차례로 붙이면 됨
        for i in range(end,end+len(temp)):
            arr[i][1:len(temp[0])+1]=temp[idx]
            idx+=1

        for I in range(start,end):                  # 원래 자기자리 초기화
            for J in range(0,j):
                arr[I][J]=0

    # =============================================
    # [4] 물고기 수 조절
    control_count()

    # [5] 한 줄로 만들기
    one_line()

    # [6] N//2 두번 회전
    temp=[]

    for i in range(N//2):           # 한번
        temp.append(arr[i][0])
        arr[i][0]=0

    idx=0
    for i in range(N-1,N//2-1,-1):  # 거꾸로 넣어준다
        arr[i][1]=temp[idx]
        idx+=1

    temp=[row[:2] for row in arr[N//2:N//2+N//4]]       # 두번
    for I in range(N//2,N//2+N//4):
        for J in range(0,2):
            arr[I][J]=0

    temp = list(map(list, zip(*temp[::-1])))            # 회전하고
    temp = list(map(list, zip(*temp[::-1])))

    idx=-1                                              # 넣어준다
    IDX=-1
    for _ in range(N//4):
        arr[idx][2:4]=temp[IDX]
        IDX-=1
        idx-=1

    # [7]번 작업
    control_count()

    # [8]번 작업
    one_line()

    # 지금까지 회전해서 봤으니 다시 원상복구
    arr=[row[:] for row in list(map(list,zip(*arr)))[::-1]]
