

from collections import deque

T=int(input())              # 테케 개수
for tc in range(1,T+1):
    # 접수 창구의 개수, 정비 창구의 개수, 방문한 총 고객의 수, (접수창구번호, 정비창구 번호)
    N,M,K,A,B=map(int,input().split())
    get=list(map(int,input().split()))
    g=[[0,0] for _ in range(N)]
    # ====================================
    fix=list(map(int,input().split()))
    f=[[0,0] for _ in range(M)]
    # ====================================
    peo=list(map(int,input().split()))
    where=[[0,0] for _ in range(K)]
    time=0
    q1=deque()
    q2=deque()

    while True:
        for k in range(K):
            if peo[k] == time:            # 만약 해당하는 시간에 들어가는 사람이 있다면
                for i in range (len(N)):
                    if f[i]==[0,0]:
                        f[i]==[k,get[i]]    # 사람이 몇번 인덱스? 시간?
                        break
                else:                       # 중간에 끊기지 않는다면
                    q1.append(k)



    print(f'{tc} {ans}')