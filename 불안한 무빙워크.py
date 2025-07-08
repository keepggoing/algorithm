''' 2차 풀이
[실수]
- 한칸 움직이기 전에도 마지막 칸에 있으면 옮겨줘야하고
한 칸 움직이고 나서도 마지막 칸에 있으면 옮겨줘야하는데

- arr=[temp[:N],temp[N:][::-1]] 여기도 뒤에 뒤집어야 하는데 안 뒤집음 정신차려
'''

def rotate(arr):
    new_arr=[[0]*N for _ in range(2)]
    new_arr[0][0]=arr[1][0]

    for j in range(1,N):
        new_arr[0][j]=arr[0][j-1]

    new_arr[1][N-1]=arr[0][N-1]

    for j in range(N-2,-1,-1):
        new_arr[1][j]=arr[1][j+1]

    arr=new_arr
    return arr

# ==============================================================
# 무빙워크의 길이 N, 실험을 종료하게 하는 판의 개수
N,K=map(int,input().split())
temp=list(map(int,input().split()))
arr=[temp[:N],temp[N:][::-1]]
peo=[[0]*N for _ in range(2)]

# 시작하기도 전에 K개 이상이면?
zero = 0
for i in range(2):
    for j in range(N):
        if arr[i][j] == 0:
            zero += 1
if zero >= K:
    print(0)

else:
    turn=1
    while True:
        arr=rotate(arr)                        # 한 칸 회전하고
        peo=rotate(peo)

        for j in range(N-1,-1,-1):             # 사람 한 칸씩 이동
            if peo[0][j]==1:
                if j==N-1:
                    peo[0][j]=0
                else:
                    if peo[0][j+1] == 0 and arr[0][j+1]>0:
                        peo[0][j]=0
                        if j+1 !=N-1:
                            peo[0][j+1]=1
                        arr[0][j+1]-=1

        if peo[0][0] == 0 and arr[0][0]>0:
            peo[0][0]=1
            arr[0][0]-=1

        zero=0
        for i in range(2):
            for j in range(N):
                if arr[i][j]==0:
                    zero+=1
        if zero>=K:
            print(turn)
            break
        turn+=1


'''
from collections import deque

N,K=map(int,input().split())
A=deque(list(map(int,input().split())))
box=deque([0]*(2*N))

phase=0
while True:
    #[1] 로봇과 함께 회전하세요
    A.appendleft(A.pop())
    box.appendleft(box.pop())

    if box[N-1]==1 :
        box[N-1]=0

    temp=[]

    # 로봇을 올리는 위치에 올리거나 로봇이 어떤 칸으로 이동하면 그 칸의 내구도는 즉시 1만큼 감소
    #[2] 이동할 수 있으면 이동한다 (바뀐것도 반영되니까 이렇게 하면 안됨)
    #가장 먼저 벨트에 올라간 로봇부터 뒤에있는 것부터 먼저하면 될듯
    for idx in range(N-1,-1,-1):
        if box[idx] == 1:
            temp.append(idx)

    for i in temp:
        if i+1<N and box[i+1]==0 and A[i+1]>=1:
            box[i]=0
            box[i+1]=1
            A[i+1]-=1
        # 항상 비어있을 거임 내려서
        if i+1==N and A[i+1]>=1:
            box[i]=0
            A[N]-=1

    #[3] 올리는 위치에 내구도가 0이 아니면 로봇 올리기
    if A[0] !=0:
        box[0]=1
        A[0]-=1

    if box[N-1]==1:
        box[N-1]=0

    #[4] 내구도가 0인게 K개 이상이면 종료 아니면 phase+=1
    phase += 1
    if A.count(0)>=K:
        break

print(phase)
'''