'''
[체감 난이도 & 총평]
골 1

[시간 복잡도]


[타임라인]


[배운점 및 실수한 점]
by 갓서현
- 완탐으로 작은 정사각형 찾는 방법 말고 길이로 찾는 방법 알고 있어야 함

'''

def find():
    for l in range(2, N + 1):
        for si in range(0, N - l + 1):
            for sj in range(0, N - l + 1):
                flag1 = False
                flag2 = False

                for i in range(si, si+l):
                    for j in range(sj, sj+l):
                        if people[i][j] == 1:
                            flag1 = True
                        if people[i][j] == 11:
                            flag2 = True

                if flag1 and flag2:
                    return si, sj, l

# =============================================================================================

N,M,K=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]  # 벽 정보만 관리하는 배열
p_loc=[tuple(map(lambda x:int(x)-1,input().split())) for _ in range(M)]       # 사람의 위치를 넣는 배열
people=[[0]*N for _ in range(N)]            # 사람이 있으면 1, 없으면 0, 출구는 11 ( 회전에 필요한 것들은 이 맵으로 )


ei,ej=map(lambda x:int(x)-1,input().split())

ans=0           # 출력할 이동 거리 합

# =============================================================================================

for _ in range(K):

    # [1-1] 모든 참가자는 동시에 움직인다 -> 동시 진행 -> 새로운 배열에 추가
    new_p_loc=[]
    for m in range(len(p_loc)):
        si,sj=p_loc[m]
        dist=abs(si-ei)+abs(sj-ej)

        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj=si+di,sj+dj
            # 범위 내, 벽 없고, 거리 줄었으면
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0  and abs(ni-ei)+abs(nj-ej)<dist:
                ans+=1                                                                      # 일단 이동은 한 거니까 +1 해주고
                if (ni,nj) != (ei,ej):                                                      # 만약 도착한 거면 그 사람은 아예 빼 !
                    new_p_loc.append((ni,nj))
                break                                                                       # 도착지든 아니든 멈춰
        else:
            new_p_loc.append((si, sj))                                                      # 못 움직인다면 그 위치 그대로 추가

    p_loc=new_p_loc[:]                                                                      # 복사

    # [1-2] 다 탈출했는지 확인 (틀린 이유)
    if len(p_loc)==0:
        break

    # [2-1] 회전하기 전에 people맵 처리
    people = [[0] * N for _ in range(N)]
    for x,y in p_loc:
        people[x][y]=1
    people[ei][ej]=11

    # [2-2] 회전할 정사각형 찾아
    si,sj,l=find()

    # [2-3] 일단 내구도 -1
    for i in range(si,si+l):
        for j in range(sj,sj+l):
            if arr[i][j]>0:
                arr[i][j]-=1

    # [2-4] 벽 맵도 사람 맵도 회전 !
    temp=[row[:] for row in arr]

    for i in range(l):
        for j in range(l):
            temp[si+i][sj+j]=arr[si+l-1-j][sj+i]
    
    # 깊은 복사 안 해도 된다 !
    arr=temp

    # [2-5] 사람 위치도 인덱스 바꿔 !
    for m in range(len(p_loc)):
        x,y=p_loc[m]
        if si<=x<si+l and sj<=y<sj+l:
            p_loc[m]=(si+(y-sj),sj+l-1-(x-si))

    # [2-6] 출구 위치도 바꿔 !
    ei,ej=(si+(ej-sj),sj+l-1-(ei-si))

print(ans)
print(ei+1,ej+1)