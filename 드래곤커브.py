'''
드래곤 커브
1. 시작점 2. 시작 방향 3. 세대

드래곤 커브의 개수 N(1 ≤ N ≤ 20)
x,y,d,g # x,y는 시작점 ( 0 인덱스 ) d는 시작 방향, g는 세대

정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 것의 개수를 고르기


격자는 무조건 100x100이고 네 꼭짓점이 모두 드래곤 커브의 일부인 정사각형의 개수를 구하기
1. 필요한 거는 드래곤 커브를 그리는 함수

x좌표 = 열, y좌표 = 행
# 우 상 좌 하

그냥 그리지 말고 좌표로 해야겠다
-> 그리고 set으로 받아서 좌표들 겹치는 거 걸러주고 -> 다 1씩 차이나는 거 있ㄴ는지 확인해서 개수세면 될 듯

좌표로 할 거니까 (x좌표, y좌표) 로 하자
dir={0:(1,0),1:(0,-1),2:(-1,0),3:(0,1)}
x,y,d,g 좌표, 방향, 세대
[1] 세대가 될 때까지 계속한다
3,3,0,1  q=deque() - append 일단 해
0세대면 방향으로 한번 간다 (d=0) 해야하는 행동 q=[0]
(3,3) (4,3)

한 번 더 재귀로 불러 리스트의 마지막 좌표가 시작 좌표고, q를 복사한다음에 시계방향으로 다 돌려
(3,4) 즉 방금 추가된 거에서 ((d+1)%4 로 하나 간다) q=[1]
(3,3) (4,3) (4,2)

4,2,1,3
3세대면
일단 0세대
(4,2) q=[1] 뽑고 돌리고 넣어
com=[2]
(4,2) (4,1) q=[1,2] 한 세대 다 했으면 덱의 순서를 반대로 바꿔 바꾸고 나서 각각의 시계방향을 하나씩 하고 추가해
# 합칠 때 반대로 rotate한다음에 넣어주면 됨

다음에는 그 안에 있는 걸 90도로 하나씩 이동한거를 append command
command=[2,3]
(4,2) (4,1) (3,1) (3,2)

# 여기서 합칠 때 command를 반대로 넣는 거임
q=[1,2,3,2]

다음에는 그걸 90도로 하나씩
command=[2,3,0,3] 이여야 하는데
(4,2) (4,1) (3,1) (3,2)

dir={0:(1,0),1:(0,-1),2:(-1,0),3:(0,1)}

1세대 q=[1,2]-> q=[2,1] 를 90도 회전 q=[3,2] 순서로 (3,1) 애서 시작
q=[2,3,2,1] -> [3,0,3,2]
(4,2) (4,1) (3,1) (3,2) (2,2) (2,3),(3,3),(3,4),(2,4)


이 규칙 맞아 !!! 잘해써

0세대에서부터 시작하구,원하는 세대 될 때까지 재귀로 반복하면 됨 !!!

총 좌표 total=set() //  토탈 좌표 (셋), 실행 해야하는 거, 몇 세대? -> 처음에 세대는 -1에서 시작함
q=deque()

# after 2세대
def drageon(generation):
    if generation == g:
        return

    command=deque()
    for i in range(q):
        command.append((q[i]+1)%4)

    for com in command:
        di,dj=dir[com]
        ni,nj=total[-1][0]+di,total[-1][1]+dj
        total.append((ni,nj))
    command.rotate(1)

    # 덱과 덱을 합친다
    q=q+command
    dragon(generation+1)

square=set()
for x,y in final:
    if (x+1,y) and (x,y+1) and (x+1,y+1) in final and ((x,y),(x+1,y),(x,y+1),(x+1,y+1)) not in square:
        square.add(((x,y),(x+1,y),(x,y+1),(x+1,y+1)))
        print(x,y)
        ans+=1
    elif (x-1,y) and (x-1,y+1) and (x,y+1) in final and ((x,y),(x-1,y),(x-1,y+1),(x,y+1)) not in square:
        print(x,y)
        ans+=1
        square.add(((x,y),(x-1,y),(x-1,y+1),(x,y+1)))
    elif (x-1,y-1) and (x,y-1) and (x-1,y) in final and ((x,y),(x-1,y-1),(x,y-1),(x-1,y)) not in square:
        square.add(((x,y),(x-1,y-1),(x,y-1),(x-1,y)))
        print(x,y)
        ans+=1
    elif (x,y-1) and (x+1,y-1) and (x+1,y) in final and ((x,y),(x+1,y-1),(x+1,y),(x,y-1)) not in square:
        print(x,y)
        square.add(((x,y),(x+1,y-1),(x+1,y),(x,y-1)))
        ans+=1
print(square)
print(ans)



내가 뭘.. 한 걸까? 왜 자꾸 오타를 가지고 1시간을 붙잡고 있는 건지 모르겠다
금방 고칠 수 있었던 거 아닐까?
'''

from collections import deque

# q는 지금까지 온 거
# command는 큐의 순서를 거꾸로 하고, 90도 회전한 거
# command를 적용해서 좌표 추가하고
# 큐+command 합친다

# after 2세대
def dragon(generation):
    global q

    if generation == g:
        return

    command = deque()
    for i in range(len(q)-1,-1,-1):
        command.append(q[i])
    # 여기서 시계 방향으로 돌리는 거고
    for i in range(len(q)):
        command[i]=(command[i] + 1) % 4

    for com in command:
        di, dj = dir[com]
        ni, nj = total[-1][0] + di, total[-1][1] + dj
        total.append((ni, nj))
    # 원래 큐와 커맨드 큐를 합친다
    # 덱과 덱을 합친다
    q = q + command
    dragon(generation + 1)

dir={0:(1,0),1:(0,-1),2:(-1,0),3:(0,1)}

# 드래곤 커브의 개수
N=int(input())

# 이건 N번 돌고 나서 합치는 거
final=set()

for _ in range(N):
    x,y,d,g=map(int,input().split())

    total = []
    q = deque()
    # 0세대 까지
    total.append((x, y))
    q.append(d)
    di, dj = dir[d]
    total.append((x + di, y + dj))
    if g > 0:
        dragon(0)
    for loc in total:
        final.add(loc)

ans=0

for i in range(100):
    for j in range(100):
        if (i,j) in final and (i+1,j) in final and (i,j+1) in final and (i+1,j+1) in final:
            ans+=1
print(ans)
