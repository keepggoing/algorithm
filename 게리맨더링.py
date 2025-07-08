N=int(input())
peop=[0]+list(map(int,input().split()))

adj=[[] for _ in range(N+1)]

for idx in range(1,N+1):
    lst=list(map(int,input().split()))

    for i in range(1,len(lst)):
        adj[idx].append(lst[i])
mn=float('inf')

from collections import deque

def check(new,other):
    v_n = set()
    q=deque([new[0]])
    v_n.add(new[0])
    sm1=peop[new[0]]

    while q:
        c=q.popleft()
        for n in adj[c]:
            if n in new and n not in v_n:
                sm1+=peop[n]
                q.append(n)
                v_n.add(n)

    if set(new) == v_n:
        v_o = set()
        q = deque([other[0]])
        v_o.add(other[0])
        sm2 = peop[other[0]]

        while q:
            c = q.popleft()
            for n in adj[c]:
                if n in other and n not in v_o:
                    sm2 += peop[n]
                    q.append(n)
                    v_o.add(n)

        if set(other) == v_o:
            return abs(sm1-sm2)

        else:
            return -1

    else:
        return -1


def btk(cnt,idx,new):
    global mn

    if cnt == num:
        other=[]
        for i in range(1,N+1):
            if i not in new:
                other.append(i)
        ans=check(new,other)
        print(ans,new,other)
        if ans != -1:
            mn=min(mn,ans)
        return

    for i in range(idx,N+1):
        if v[i] == 0:
            v[i]=1
            new.append(i)
            btk(cnt+1,i+1,new)
            new.pop()
            v[i]=0

for num in range(1,N//2+1):
    v=[0]*(N+1)
    btk(0,1,[])

if mn == float('inf'):
    print(-1)
else:
    print(mn)

# 두 선거구로 나누었을 때 인구 차이의 최솟값
# 나눌 수 없다면 -1 출력

# 인접한 구역 없을 수도 있고 ( 즉 혼자 떨어져있기 가능 )
# 인접한 구역의 수, 인접한 구역의 번호

# 구역의 개수
N=int(input())
peop=list(map(int,input().split()))

adj=[[] for _ in range(N+1)]

for idx in range(1,N+1):
    lst=list(map(int,input().split()))

    for i in range(1,len(lst)):
        adj[idx].append(lst[i])

# =================
def btk(cnt,idx,lst1,lst2):
    global num
    if cnt == N:
        print(lst1)
        print(lst2)
        return

    for i in range(idx,N+1):
        if v[i]==0:
            if len(lst1)<num:
                lst1.append(i)
                v[i] = 1
                btk(cnt + 1,i+1, lst1, lst2)
                v[i] = 0
                lst1.pop()
            else:
                lst2.append(i)
                v[i] =1
                btk(cnt+1,i+1,lst1,lst2)
                v[i]=0
                lst2.pop()


# 구역을 몇개로 나눌건지 다양한 경우가 있지
for num in range(1,N//2+1):
    # 구역의 개수는 이렇게 두 조합으로
    v=[0]*(N+1)
    btk(0,1,[],[])

''' 잘 모르겠다./
N=int(input())
peop=list(map(int,input().split()))

adj=[[] for _ in range(N+1)]

for idx in range(1,N+1):
    lst=list(map(int,input().split()))

    for i in range(1,len(lst)):
        adj[idx].append(lst[i])

from collections import deque

def check(i,j):
    sm1,q1=deque([(peop[i],i)])
    sm2,q2=deque([(peop[j],j)])

    v=[0]*(N+1)
    
    while q1 or q2:
        c1=q1.popleft()
        c2=q2.popleft()
        
        for idx in adj[c1]:
            if v[idx] == 0:
                v[idx]=1
                q1.append([(sm1+peop[idx],)])
                
        for idx in adj[c2]:
            if v[idx]==0:
                v[idx]=1

for i in range(1,N+1):
    for j in range(i+1,N+1):
        # 기준 큐를 두개 정한다
        check(i,j)
'''