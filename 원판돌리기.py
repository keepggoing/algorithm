'''
13퍼에서 틀렸습니다.. 인데 화장실 다녀와서 찾잨
'''
from collections import deque
# N개의 원판, 각각에 M개의 수
N,M,T=map(int,input().split())
arr=[deque(map(int,input().split())) for _ in range(N)]
#print('------ 0단계 : 기본')
#for row in arr:
#    print(*row)
# T번의 명령을 진행
for _ in range(T):
    # x의 배수인 걸 d방향으로 k칸 회전
    x,d,k=map(int,input().split())

    for idx in range(0,N):
        # x의 배수인 것만 돌린다
        if (idx+1)%x == 0:
            if d==0: # 시계방향
                for _ in range(k):
                    arr[idx].rotate(1)
            elif d==1: # 반시계방향
                for _ in range(k):
                    arr[idx].rotate(-1)
    #print('------ 1단계 : 회전한다')
    #for row in arr:
    #    print(*row)

    # 자 이제 내가 해야하는 건 인접하면서 수가 같은 것을 모두 찾는 거
    flag = False
    v = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            # 0이 아니고 방문 안 했을 때만
            if arr[i][j] !=0 and v[i][j]==0:
                # 이게 시작점이고
                si,sj=i,j
                q=deque([(si,sj)])
                v[si][sj]=1
                lst=[]
                pivot = arr[si][sj]

                while q:
                    ci,cj=q.popleft()
                    lst.append((ci,cj))
                    if ci==0:
                        for di,dj in ((1,0),(0,-1),(0,1)):
                            ni,nj=(ci+di)%N,(cj+dj)%M
                            if arr[ni][nj]==pivot and v[ni][nj]==0:
                                q.append((ni,nj))
                                v[ni][nj]=1

                    elif ci==N-1:
                        for di,dj in ((-1,0),(0,-1),(0,1)):
                            ni,nj=(ci+di)%N,(cj+dj)%M
                            if arr[ni][nj]==pivot and v[ni][nj]==0:
                                q.append((ni,nj))
                                v[ni][nj]=1

                    else:
                        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                            ni,nj=(ci+di)%N,(cj+dj)%M
                            if arr[ni][nj]==pivot and v[ni][nj]==0:
                                q.append((ni,nj))
                                v[ni][nj]=1
                if len(lst)!=1:
                    for x,y in lst:
                        arr[x][y]=0
                    flag = True

    # 다 돌았는데도 flag가 안 바뀌면
    # 원판에 적힌 수의 평균을 구하고 돌면서 평균보다 큰 수+1, 작은수-1
    if not flag:
        sm=sum(map(sum,arr))
        cnt=0
        for i in range(N):
            for j in range(M):
                if arr[i][j] != 0:
                    cnt+=1
        if cnt != 0:
            mn=sm/cnt

            #print(mn)
            for i in range(N):
                for j in range(M):
                    if arr[i][j]!=0:
                        if arr[i][j]>mn:
                            arr[i][j]-=1
                        elif arr[i][j]<mn:
                            arr[i][j]+=1
    #print('------ 2단계 : 같은 거 있는지 확인하고 나서 ')
    #for row in arr:
    #    print(*row)
# 구하는 건 T번 회전 후 원판에 적힌 수의 합
print(sum(map(sum,arr)))