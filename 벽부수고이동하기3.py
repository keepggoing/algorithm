'''
visited를 이미 세개를 부셧는데 하나도 갈 수 있는걸 재방문할 필요가 없닥고?
세개 부신게 필요가 없어지는 거 <- 시간이 똑같다는 전제 하여야지
-> 노드 재방문에 대해서 생각한거지 쓸데없는 걸 여러번 반복하지 않ㄹ도록

낮밤이 의미가 있나?
두개를 통일을 하고 정지
'''

N,M,K=map(int,input().split())
arr=[list(map(int,input())) for _ in range(N)]
v=[[K+1 for _ in range(M)] for _ in range(N)]
from collections import deque

# 시간, 얼마나 뿌셨는지, 좌표
q=deque([(1,0,0,0)])
v[0][0]=0

while q:
    time,broke,ci,cj=q.popleft()

    if (ci,cj) == (N-1,M-1):
        print(time)
        break

    for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni,nj=ci+di,cj+dj
        if 0<=ni<N and 0<=nj<M:
            # 왜 또 인자에 가지고 다녀야 하냐? 가장 최적의 수가 v에 잇는 거지
            # 그건 v에 접근하는 애들만 막고 싶은 건데, 더 안 좋은 경우는 가지치기 해주려고
            # 근데 다음 노드로 갈 때는 가지고 있는 거로 해야지
            # time은 두개다 쓰는게 쓸데없는 거 엿자나 근데 지금은 두개 다 써야하고
            # 그 이유가 time은 바뀌지 않는데,즉 재방문이 안 되는 건데
            # 지금은 재방문이 되니ㅣ까ㅏㅏㅏ
            # 지금가지 온 거를 바ㅏ꿔버리네 ..
            # ci,cj를 큐에 넣은 거랑 나중에 v[ci][cj]
            # v[ni][nj]를 정해줄 때 더 적은 거로 하는게 좋지
            # broke+1 v[ci][cj]+1
            if arr[ni][nj] == 1 and v[ni][nj]>broke+1:
                if time % 2 == 0:
                    q.append((time+1,broke+1,ci,cj))

                else:
                    q.append((time+1,broke+1,ni,nj))
                    v[ni][nj]=broke+1

            elif arr[ni][nj] == 0 and v[ni][nj]>broke:
                q.append((time+1,broke,ni,nj))
                v[ni][nj]=broke
else:
    print(-1)

# 시간 기록할때 말고 여러번 같은 노드를 방문할 때 갱신하면서 사용한 적이 없었지
# 써본 적 없는 걸
#
'''
N,M,K=map(int,input().split())
arr=[list(map(int,input())) for _ in range(N)]
# 시간, 벽 부순 개수 -> 같은 곳에 도달했을 때 시간이 더 작다면 바꾸고, 시간이 같다면 벽 부순 개수가 더 적을 때 바꾼다
# 만약 시간도 같고, 벽 부순 개수도 같으면? -> 보류
# 밤일 때 벽은 못 부수니까 시간을 하나 더 더해서 낮으로 바꿈
# 시간이 항상 동일하게 들어가는 거 아니니까 만나자마자 종료하는게 아니라 끝까지 봄
# 근데 시간이 더 오래걸리지만 벽 부순 개수가 더 적어서 최종적으론 시간이 덜 걸리는 경우가 있을 수 있겠지?
# 그래서 시간 기준으로 짤라버리면 예외가 생기겠네 -> 벽 부순 개수로 자르면?
# 같은 자리를 더 많은 벽을 부수고 왔어 근데 시간은 더 짧아 -> 나중에 더 짧아질 수 있으니 이거로도 기준을 하면 안 될 듯
# 그럼 벽 부순 개수가 같을 때만 시간 비교해서 처리해주기
# 근데 또 고민되는 건 밤이냐 낮이냐를 아까 하던대로 처리해도 되는지?
# 아니면 이렇게 아예 바꿔서 해봐야 하는지 v[i][j][부순 개수][낮/밤],
# 기준을 내맘대로 섞으면 안 되고 아예 모든게 같은 상황일 때 시간이 더 걸리는 거만 짜르기
# ==============================================
# v[i][j][부순 개수][낮/밤]
# 부순 개수에 거꾸로도 가는게 문제인거지 ci,cj에서 낮이였으면 ni,nj는 밤이니까 밤이랑 비교를 해야
# 낮,밤
# 시간도 더 크고 부순 개수도 더 크면 못 간다

v=[[[0 for _ in range(K+1)] for _ in range(M)] for _ in range(N)]

from collections import deque
# 시간,낮0 밤1, 몇개 부숨, 좌표
q=deque([(1,0,0,0,0)])
# 안 부수고 시작
v[0][0][0]=1

while q:
    time,day,broke,ci,cj=q.popleft()

    if (ci,cj) == (N-1,M-1):
        print(time)
        for row in v:
            print(*row)
        break

    for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni,nj=ci+di,cj+dj
        if 0<=ni<N and 0<=nj<M:
            # K랑 체크는 해야지
            # 지금은 낮인데, 다음은 밤이니까 밤이랑 비교를 해야지
            # 근데 밤으로 들어갈건데 만약 낮이 더 작으면 넣을 필요가 없겠지?
            # 같은 위치를 더 많은 블록 개수로 갈 필요는 없음
            if arr[ni][nj]==1 and broke+1<=K:
                if day==0 and v[ni][nj][broke+1]>time+1:
                    v[ni][nj][broke+1]=time+1
                    q.append((time+1,1,broke+1,ni,nj))

                elif day==1:       # 이 부분 때문에 두개로 나눠야 한다고 생각함, 그리고 하나로 하면
                    v[ci][cj][broke]=time+1
                    q.append((time+1, 0, broke, ci, cj))

            elif arr[ni][nj]==0 and v[ni][nj][broke]>time+1:
                v[ni][nj][broke]=time+1
                q.append((time+1,1,broke,ni,nj))
else:
    print(-1)

벽 부순 개수로 나누면 반대로 가는 문제가 생김
막는 방법이 있겠지..

같은 부순 개수 말고 그 이상만 보면 되나?

'''