''' 2차 풀이
[실수한 점]
도망자 -> 술래 겹치는 칸으로 움직이진 못하지만
술래 -> 도망자 겹치는 칸으로는 이동 가능

둘은 같은 곳에 있을 수 없다고만 생각하고 for mul in (0,1,2): 이 부분에서 0을 빼줌

[소요시간]
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

print(score)

'''
[체감 난이도 & 총평]
[구상]
-
[시간 복잡도]
[주의할 점]
[타임라인]
0900~0915
0915~0940
[추가 TC]


트리 위치를 set()으로 관리
인덱스를 빼지않고 False로 바꿔줘도 됨

'''

# 안->밖 달팽이 ( 방향은 시계방향으로 바뀜 )
def sul1():
    si,sj,dr=n//2,n//2,0
    man.append((si,sj,dr))
    dist=1

    while True:
        for _ in range(2):
            for k in range(1,dist):
                si,sj=si+di[dr],sj+dj[dr]
                if (si,sj) == (0,0):
                    return
                man.append((si,sj,dr))
            si, sj = si + di[dr], sj + dj[dr]       # dist-1까지 돌려주고 마지막 꺼는 루프 나와서 추가
            dr=(dr+1)%4
            man.append((si, sj, dr))
        dist+=1

# 밖-> 안 달팽이 ( 방향은 반시계방향으로 바뀜 )
def sul2():
    v=[[0]*n for _ in range(n)]                     # visited로 방향 꺽어줌
    si,sj,dr=0,0,2
    v[si][sj]=1
    man.append((si,sj,dr))

    while (si,sj) != (n//2, n//2):
        si,sj=si+di[dr],sj+dj[dr]
        if si<0 or si>=n or sj<0 or sj>=n or v[si][sj]==1:      # 범위 밖이거나 방문했던 곳이먄
            si, sj = si - di[dr], sj - dj[dr]                   # 다시 원래 위치로 오고
            dr=(dr-1)%4                                         # 방향 바꿔주고
        else:
            # 가장 끝 턴이면
            if si+di[dr] < 0 or si+di[dr] >= n or sj+dj[dr] < 0 or sj+dj[dr] >= n or v[si+di[dr]][sj+dj[dr]] == 1:
                man.append((si,sj,(dr-1)%4))
            else:
                man.append((si,sj,dr))
            v[si][sj]=1
    man.pop()

# ================================================================
# nxn 격자, 도망자의 수, 나무의 개수, k번의 술래잡기
n,m,h,k=map(int,input().split())
arr=[[[] for _ in range(n)] for _ in range(n)]  # arr에는 도망자의 인덱스가 들어감
loc=[[] for _ in range(m)]                     # loc의 도망자 인덱스에는 (x좌표, y좌표, 방향) 들어감
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

tree=set()                              # 특정 좌표에 나무가 있냐 없냐 확인할 거기 때문에 set으로 관리
for _ in range(h):
    x,y=map(int,input().split())
    x,y=x-1,y-1
    tree.add((x,y))

# 정답
ans=0

# 술래 ( x좌표, y좌표, 방향 )
man=[]
sul1()
sul2()
# 이제 man에는 술래 위치, 방향이 다 정해져있고, idx로 쭉 돌리면 됨
idx=0
M=len(man)

# ===================================================

for t in range(1,k+1):
    si,sj,_=man[idx]       # 이게 술래의 위치

    # [1] 도망자 한명씩 움직인다
    for i in range(len(loc)):
        x,y,d = loc[i]
        if abs(si-x)+abs(sj-y)<=3:      # 3칸 이하일 때
            ni,nj=x+di[d],y+dj[d]
            if 0<=ni<n and 0<=nj<n:     # 격자를 벗어나지 않는 경우에
                if (ni,nj) != (si,sj):  # 술래의 위치가 아닐 때만 움직인다
                    loc[i] = [ni,nj,d]  # loc에 새로운 위치 반영해주고
                    arr[x][y].remove(i)
                    arr[ni][nj].append(i)   # arr에도 반양해준다
            else:                       # 격자를 벗어나는 경우에는 방향 반대로 틀고
                d=(d+2)%4
                ni,nj=x+di[d],y+dj[d]
                if (ni,nj) != (si,sj):  # 술래의 위치가 아닐 때 또 같은 단위작업 한다
                    loc[i] = [ni,nj,d]
                    arr[x][y].remove(i)
                    arr[ni][nj].append(i)

                else:
                    loc[i] = [x,y,d]    # 술래랑 겹친다면 방향만 바꿔서 넣어준다

    # =====================================

    # [2] 술래가 움직인다
    idx=(idx+1)%M
    si,sj,sd=man[idx]

    # =====================================
    # [3] 3칸 안에 있는 도망자를 본다
    # 술래랑 겹칠 수도 있지?
    for mul in (0,1,2):
        nni,nnj=si+di[sd]*mul,sj+dj[sd]*mul
        # 범위 내에 있고, 나무 없고, 도망자 있다면 잡는 거
        if 0<=nni<n and 0<=nnj<n and (nni,nnj) not in tree and arr[nni][nnj] != []:
            ans+=t*(len(arr[nni][nnj]))
            for num in arr[nni][nnj]:                         # 잡힌 도망자는
                loc[num]=[100,100,100]                        # loc에서도 쓰레기값 [100,100,100]으로 바꾸고
                arr[nni][nnj]=[]                              # arr 맵에서도 없어지고

print(ans)
