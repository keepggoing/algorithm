''' 2차풀이
[0] 타임라인
구상 (20분)
구현 (30분)
디버깅 (15분)

[1] 실수한점
1. 도망자 -> 술래 겹치는 칸으로 움직이진 못하지만, 술래 -> 도망자 겹치는 칸으로는 이동 가능
둘은 같은 곳에 있을 수 없다고만 생각하고 for mul in (0,1,2): 이 부분에서 0을 빼줌

[2] 배울점
'''
# 격자 크기 NxN, M명의 도망자, H개의 나무, K턴
N,M,H,K=map(int,input().split())
p_loc=[]
p=[[[] for _ in range(N)] for _ in range(N)]
tree=[[0]*N for _ in range(N)]

for idx in range(M):
    x,y,d=map(int,input().split())
    x,y=x-1,y-1
    p[x][y].append(idx)
    p_loc.append([False,x,y,d])

for _ in range(H):
    x,y=map(lambda x:int(x)-1,input().split())
    tree[x][y]=1

score=0
# 순서대로 상, 우, 하,좌
dic={0:(-1,0),1:(0,1),2:(1,0),3:(0,-1)}

# =============================
si,sj=N//2,N//2
sd=0
directions=[sd]
locations=[(si,sj)]

cnt=1
flag=False

while True:
    for _ in range(2):
        for mul in range(cnt):
            di,dj=dic[sd]
            si,sj=si+di,sj+dj

            locations.append((si,sj))
            if mul == cnt-1:
                directions.append((sd+1)%4)
            else:
                directions.append(sd)
            if (si,sj) == (0,0):
                flag=True
                break
        if flag:
            break
        sd=(sd+1)%4
    if flag:
        break
    cnt+=1
locations.extend(locations[1:len(locations)-1][::-1])
directions.pop()
directions.append(2)
directions.extend((i+2)%4 for i in directions[:len(directions)-2][::-1])
L=len(locations)
# ================================================
def my_print():
    print('술래 위치와 방향')
    print(si,sj,sd)
    print('도망자 맵')
    for row in p:
        print(*row)
    print('도망자 위치')
    print(p_loc)
    print("====")

sidx=0
# [0] 술래의 위치
si, sj = locations[sidx % L]
sd = directions[sidx % L]

for turn in range(1,K+1):       # K턴 동안
    # [1] 도망자의 움직임
    for idx in range(M):
        if p_loc[idx][0]==False:
            flag,mi,mj,md=p_loc[idx]
            if abs(si-mi)+abs(sj-mj) <= 3:
                di,dj=dic[md]
                ni,nj=mi+di,mj+dj

                if 0<=ni<N and 0<=nj<N:             # 범위 내라면
                    if (si,sj) != (ni,nj):
                        p_loc[idx]=[False,ni,nj,md]
                        p[mi][mj].remove(idx)
                        p[ni][nj].append(idx)

                else:                               # 범위 밖이라면
                    md=(md+2)%4
                    di,dj=dic[md]
                    ni,nj=mi+di,mj+dj
                    if (si,sj) != (ni,nj):
                        p_loc[idx]=[False,ni,nj,md]
                        p[mi][mj].remove(idx)
                        p[ni][nj].append(idx)
    #print(turn)
    #print('도망자 움직이고 나서')
    #my_print()
    # [2] 술래의 움직임
    sidx+=1
    si,sj=locations[sidx%L]
    sd = directions[sidx%L]
    di,dj=dic[sd]
    for mul in (0,1,2):
        ni,nj=si+mul*di,sj+mul*dj
        if 0<=ni<N and 0<=nj<N and p[ni][nj] != [] and tree[ni][nj]==0:         # 누군가 있고, 나무가 없다면
            score+=turn*len(p[ni][nj])
            for idx in p[ni][nj]:
                p_loc[idx]=[True,-1,-1,-1]
            p[ni][nj]=[]
    #print(turn)
    #print('술래 움직이고 나서')
    #my_print()

print(score)


'''
코드트리 술래잡기 / 2025-03-21 / 체감 난이도 : 골드 1
소요 시간 : 1시간 30분 / 시도 : 1회

[0] 총평
- 문제 풀면서 도망자 관리하는 자료형을 많이 바꿔서 너무 헷갈렸다
- 하지만 나처럼 arr이랑 loc 둘다 운영하지 않고

[1] 타임라인
1. 문제 이해 & 구상 & 입력받기 (20분)
2. 달팽이 구현 (30분)
3. 나머지 구현 (25분)
4. 디버깅 (15분)
-> 오픈테케 답 잘못나옴
다 잘 나오는데 답만 이상하게 나와서 답에 더할 때 aar[nnj][nnj] 오타 있는 것을 발견

[2] 배운점 및 실수한 점

[3] 시간 복잡도
sul에서 격자 두번 도니까 50*50*2
최대 k번 돌고 그 안에서는 최대 2500번 돈다

5000 + 100*2500
10^4 * 상수 시간

[4] 엣지케이스

'''

def sul():
    si,sj,dr=n//2,n//2,0
    # 처음 방향에서 위를 보고 있다
    man.append((si,sj,dr))
    dist=1
    flag=False

    while True:
        for _ in range(2):
            for k in range(1,dist+1):
                if (si,sj) == (0,0):
                    flag=True
                    break
                si,sj=si+di[dr],sj+dj[dr]
                if k != dist:
                    man.append((si, sj, dr))
            if flag:
                break
            dr=(dr+1)%4
            man.append((si, sj, dr))
        if flag:
            break
        dist+=1

    # 처음 위치에 멈추면
    man.pop()

    # 두번째
    v=[[0]*n for _ in range(n)]
    si,sj,dr=0,0,2
    v[si][sj]=1
    man.append((si,sj,dr))

    while (si,sj) != (n//2, n//2):
        si,sj=si+di[dr],sj+dj[dr]
        if si<0 or si>=n or sj<0 or sj>=n or v[si][sj]==1:
            si, sj = si - di[dr], sj - dj[dr]       # 다시 원래 위치로 오고
            dr=(dr-1)%4                             # 방향 바꿔주고
        else:
            if si+di[dr] < 0 or si+di[dr] >= n or sj+dj[dr] < 0 or sj+dj[dr] >= n or v[si+di[dr]][sj+dj[dr]] == 1:
                man.append((si,sj,(dr-1)%4))
            else:
                man.append((si,sj,dr))
            v[si][sj]=1
    man.pop()
    print(man)

# ==============================================================
# nxn 격자, 도망자의 수, 나무의 개수, k번의 술래잡기
n,m,h,k=map(int,input().split())
arr=[[[] for _ in range(n)] for _ in range(n)]
loc=[[] for _ in range(m)]
# 상,우,하,좌
di=[-1,0,1,0]
dj=[0,1,0,-1]

for i in range(m):
    x,y,d=map(int,input().split())
    x,y=x-1,y-1
    if d == 1:      # 좌우로 움직임 (우로 시작)
        loc[i]=[x,y,1]
        arr[x][y].append(i)
    elif d == 2:    # 상하로 움직임 (하로 시작)
        loc[i]=[x,y,2]
        arr[x][y].append(i)

tree=set()
for _ in range(h):
    x,y=map(int,input().split())
    x,y=x-1,y-1
    tree.add((x,y))

# 정답
ans=0

# 술래 ( x좌표, y좌표, 방향 )
man=[]
sul()
# 이제 man에는 움직이는 방향 다 정해져있고 idx로 정해서 쭉 돌리면 됨
idx=0
M=len(man)

# ================================================== 입력 받기 완료
for t in range(1,k+1):
    si,sj,_=man[idx]       # 이게 술래의 위치

    for i in range(len(loc)):
        x,y,d = loc[i]
        if abs(si-x)+abs(sj-y)<=3:      # 3칸 이하일 때
            ni,nj=x+di[d],y+dj[d]
            if 0<=ni<n and 0<=nj<n:     # 격자를 벗어나지 않는 경우에
                if (ni,nj) != (si,sj):  # 술래의 위치가 아닐 때만  움직인다
                    loc[i] = [ni,nj,d]
                    arr[x][y].remove(i)
                    arr[ni][nj].append(i)
            else:                       # 격자를 벗어나는 경우에는
                d=(d+2)%4
                ni,nj=x+di[d],y+dj[d]
                if (ni,nj) != (si,sj):
                    loc[i] = [ni,nj,d]
                    arr[x][y].remove(i)
                    arr[ni][nj].append(i)

                else:
                    loc[i] = [x,y,d]    # 술래랑 겹친다면 방향만 바꿔서 넣어준다

    # =====================================

    # 술래가 움직인다
    idx=(idx+1)%M
    si,sj,sd=man[idx]

    # =====================================
    # 3칸을 본다
    # 술래랑 겹칠 수도 있지?
    for mul in (0,1,2):
        nni,nnj=si+di[sd]*mul,sj+dj[sd]*mul
        # 범위 내에 있고, 나무 없고, 도망자 있다면 잡는 거
        if 0<=nni<n and 0<=nnj<n and (nni,nnj) not in tree and arr[nni][nnj] != []:
            ans+=t*(len(arr[nni][nnj]))
            for num in arr[nni][nnj]:
                loc[num]=[100,100,100]                        # loc에서도 쓰레기값 [100,100,100]으로
                arr[nni][nnj]=[]                              # arr 맵에서도 없어지고

print(ans)