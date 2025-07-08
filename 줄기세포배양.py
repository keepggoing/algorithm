'''
max를 자꾸 비교하고 계속 넣고 있었음 최종 하나만 넣어야 하는데
'''

T=int(input())
for tc in range(1,T+1):
    # N은 행, M은 열, K는 시간
    N,M,K=map(int,input().split())
    k=K//2+1

    arr=[[0]*(2*k+M) for _ in range(k)]+[[0]*k +list(map(int,input().split()))+[0]*k for _ in range(N)]+[[0]*(2*k+M) for _ in range(k)]
    N=N+2*k
    M=M+2*k

    dic={}
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                if arr[i][j] in dic:
                    dic[arr[i][j]].append((i,j))
                else:
                    dic[arr[i][j]]=[(i,j)]

    lst=[]
    activated={}
    #print('비활성화된 거 dic',dic)
    #print('복제해야하는 거 lst',lst)
    #print('활성화된 거',activated)

    # ========================
    # dic에는 비활성화된 게 있고
    # lst에는 복제해야할게 있고
    # activated에는 활성화된게 있음

    for time in range(1,K+1):
        if lst:                                                     # 즉 복제시킬게 있다면
            new_arr=[row[:] for row in arr]                         # 새로운 배열에
            new={}
            for si,sj in lst:                                       # 하나하나
                for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):           # 4방향으로 할 건데
                    ni,nj=si+di,sj+dj
                    if 0<=ni<N and 0<=nj<M and arr[ni][nj]==0:      # 범위 내이고 비어있을 때만 가능
                        if new_arr[ni][nj]<arr[si][sj]:
                            new_arr[ni][nj]=arr[si][sj]             # 뭔가 미리 있다면 더 큰 거로 해야하니까
                            new[(ni,nj)]=time+arr[si][sj]

            for key,value in new.items():
                if value in dic:
                    dic[value].append(key)
                else:
                    dic[value]=[key]

            arr=new_arr                                             # 바꿔치기 하고
            lst=[]                                                  # lst는 다시 비워줌

        if activated:                                               # 활성화된게 있다면 하나씩 빼줘야함
            new_activated={}
            for key,value in activated.items():
                if key-1 == 0:                                      # 0이 되면 **** 이 부분이 틀림 *****
                    for x,y in value:                               # -1로 바꾸고 끝
                        arr[x][y]=-1
                else:
                    new_activated[key-1]=value                      # 아니면 하나 줄여서 넣어주고
            activated=new_activated                                 # 바꿔치기

        if time in dic:                                             # 또 활성화 해야할게 있다면
            lst.extend(dic[time])                                   # lst에 넣어주고 이건 다음 턴에 복제할 거니까
            #real_time=arr[dic[time][0][0]][dic[time][0][1]]         # 실제 시간은 다를 수가 있구나
            for x,y in dic[time]:                                   # 활성화 할 때는 실제 시가능로
                if arr[x][y] in activated:
                    activated[arr[x][y]].append((x,y))
                else:
                    activated[arr[x][y]]=[(x, y)]
            #print(dic)
            #print(time)
            del dic[time]                                           # dic에서는 지움
            #print(dic)
        #print(time)
        #print('활성화된 거',activated)

    ans=0
    for i in range(N):
        for j in range(M):
            if arr[i][j]>0:
                ans+=1
    print(f'#{tc} {ans}')