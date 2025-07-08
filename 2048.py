''' 2차 풀이
[1] 소요시간 : 50분 ( 20분 구상 - 25분 구현 - 5분 디버깅 )
[2] 고려한 점 : 방향만 다르지 사실은 게임에서 하는 행위는 동일하다는 것을 인지하고, 이를 하나로 구현하고자함
1차 풀이에서는 중력 느낌으로 구현했는데, 이번에는 이 문제에 맞게 구현해봄
[3] 실수 : 배열을 매개변수로 갖고 다니는 걸 처음 활용해봤는데, 원상복구를 하고 있었음
원상복구를 안 하려고 temp에다가 arr을 복사해서 처리 다 한 다음에, btk 함수를 나오면 저절로 arr에는 원래 배열이 있으니까
복구를 안 해줘도 되는 것임
[4] 시간복잡도 : btk 함수 4**5 -> 2**10 이고 move 함수 최대 20번 정도 돈다
'''

def move(arr):
    for i in range(n):
        lst = arr[i]
        new = []
        idx = 0
        pivot = -1
        while idx < n:
            if lst[idx] == 0:
                idx += 1
            else:
                if pivot != lst[idx]:
                    if pivot != -1:
                        new.append(pivot)
                    pivot = lst[idx]
                else:
                    new.append(pivot * 2)
                    pivot = -1
                idx += 1

        if pivot != -1:
            new.append(pivot)
        new += [0] * (n - len(new))
        arr[i] = new
    return arr

# arr을 매개변수로 들고 들어간다
def btk(cnt,arr):
    global mx

    if cnt==5:
        mx=max(mx,max(map(max,arr)))
        return

    # move 하기 전을 복사해두고
    temp=[row[:] for row in arr]
    move(temp)
    btk(cnt+1,temp)

    temp=[row[::-1] for row in arr]
    move(temp)
    btk(cnt+1,temp)

    # 이젠 전치해야댐
    arr_t=list(map(list,zip(*arr)))
    temp=[row[:] for row in arr_t]
    move(temp)
    temp=list(map(list,zip(*temp)))
    btk(cnt+1,temp)

    temp=[row[::-1] for row in arr_t]
    move(temp)
    temp=list(map(list,zip(*temp)))
    btk(cnt+1,temp)

n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
mx=-1

btk(0,arr)
print(mx)

'''
B12100 2048(Easy) / 2025-03-17 / 체감 난이도 : 골드 2
소요 시간 : 1시간 25분 / 시도 : 2회

[0] 총평
- 손으로 구상하는 것도 상하좌우 별 유닛테스트도 잘 먹혔다 !


[1] 타임라인
1. 문제 이해 및 큰그림 구상 (15분)
2. 구현 (40분)
3. 디버깅 & 문제 예시로 한 번 더 확인 (10분)
- 배열이랑 숫자랑 연산하고 있어서 뭐가 안 된다는 오류가 자꾸 떴는데
arr = [row[:] for row in temp] 이렇게 써야하는 걸 arr = [temp[:] for row in temp] 이렇게 쓰고 있었음
- ans=max(ans,max(map(max,arr))) 배열의 max를 ans와 한 번 더 비교해줘야 하는데
  ans=max(map(max,arr)) 이렇게 그냥 할당만 해버림

4. 실패 후 다시 디버깅 (15분)
- 종료 조건을 6으로 하고 있었음 0번부터 시작했으니까 5번에 끝나야함
종료 조건에 몇번 가는지 변수 찍어서 2**12 가 되는 걸 발견

[2] 배운점 및 실수한 점
- 사실 이 문제도 네 방향 모두 같은 행동을 하니까 하나의 행동으로 만들 수 있음 !! (교수님 코드 참조)

'''
def move(dr, arr):
    di, dj = dic[dr]
    v = [[0] * N for _ in range(N)]

    if dr == 0:
        for j in range(N):
            for i in range(1, N):
                # 일단 내가 0이 아니고
                if arr[i][j] != 0:
                    while True:
                        if i + di < 0 or i + di >= N or j + dj < 0 or j + dj >= N:
                            break
                        elif arr[i + di][j + dj] == 0:
                            arr[i + di][j + dj] = arr[i][j]
                            arr[i][j] = 0
                            i, j = i + di, j + dj
                        elif arr[i + di][j + dj] == arr[i][j] and v[i + di][j + dj] == 0:
                            arr[i + di][j + dj] *= 2
                            arr[i][j] = 0
                            v[i + di][j + dj] = 1
                            break
                        else:
                            break

    elif dr == 1:
        for j in range(N):
            for i in range(N - 2, -1, -1):
                if arr[i][j] != 0:
                    while True:
                        if i + di < 0 or i + di >= N or j + dj < 0 or j + dj >= N:
                            break
                        elif arr[i + di][j + dj] == 0:
                            arr[i + di][j + dj] = arr[i][j]
                            arr[i][j] = 0
                            i, j = i + di, j + dj
                        elif arr[i + di][j + dj] == arr[i][j] and v[i + di][j + dj] == 0:
                            arr[i + di][j + dj] *= 2
                            arr[i][j] = 0
                            v[i + di][j + dj] = 1
                            break
                        else:
                            break
    elif dr == 2:
        for i in range(N):
            for j in range(1, N):
                if arr[i][j] != 0:
                    while True:
                        if i + di < 0 or i + di >= N or j + dj < 0 or j + dj >= N:
                            break
                        elif arr[i + di][j + dj] == 0:
                            arr[i + di][j + dj] = arr[i][j]
                            arr[i][j] = 0
                            i, j = i + di, j + dj
                        elif arr[i + di][j + dj] == arr[i][j] and v[i + di][j + dj] == 0:
                            arr[i + di][j + dj] *= 2
                            arr[i][j] = 0
                            v[i + di][j + dj] = 1
                            break
                        else:
                            break
    elif dr == 3:
        for i in range(N):
            for j in range(N - 2, -1, -1):
                if arr[i][j] != 0:
                    while True:
                        if i + di < 0 or i + di >= N or j + dj < 0 or j + dj >= N:
                            break
                        elif arr[i + di][j + dj] == 0:
                            arr[i + di][j + dj] = arr[i][j]
                            arr[i][j] = 0
                            i, j = i + di, j + dj
                        elif arr[i + di][j + dj] == arr[i][j] and v[i + di][j + dj] == 0:
                            arr[i + di][j + dj] *= 2
                            arr[i][j] = 0
                            v[i + di][j + dj] = 1
                            break
                        else:
                            break

def btk(cnt, arr):
    global ans

    if cnt == 5:
        ans = max(ans, max(map(max, arr)))
        return

    for dr in range(4):
        temp = [row[:] for row in arr]
        move(dr, arr)
        btk(cnt + 1, arr)
        arr = [row[:] for row in temp]


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

# 상하좌우 순서
dic = {0: (-1, 0), 1: (1, 0), 2: (0, -1), 3: (0, 1)}
btk(0, arr)
print(ans)

''' 맵을 돌리는 버전
def move(arr):
    for i in range(len(arr)):
        # 앞에서부터 하나씩 보면서 비교하는 값을 갱신 
        pivot=0
        tp=[]
        for n in arr[i]:
            if n==0:
                continue
            # pivot이랑 같으면 합쳐야지
            if n==pivot:
                tp.append(pivot*2)
                # 이미 합쳐진 건 더이상 건들면 안 되니까
                pivot=0
            else:
                # pivot이랑 달라
                # 0이 아니라면 pivot을 이제 넣어주고 바꿔줌
                if pivot!=0:
                    tp.append(pivot)
                pivot=n
        # pivot 아직 남아있으면        
        if pivot>0:
            tp.append(pivot)
        arr[i]=tp+[0]*(N-len(tp)


def btk(cnt, arr):
    global ans

    if cnt == 5:
        ans=max(ans,max(map(max,arr)))
        return

    # 좌측으로 이동
    temp=[row[:] for row in arr]
    move(temp)
    btk(cnt+1,temp)
    # 여기서 안 바꿔도 되는 이유는 arr은 그대로이기 때문

    # 우
    temp=[row[::-1] for row in arr]
    move(temp)
    btk(cnt+1,temp)

    # 상
    arr_t=list(map(list,zip(*arr)))
    temp=[row[:] for row in arr_t]
    move(temp)
    btk(cnt+1,temp)

    # 하
    temp=[row[::-1] for row in arr_t]
    move(temp)
    btk(cnt+1,temp)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

btk(0, arr)
print(ans)
'''