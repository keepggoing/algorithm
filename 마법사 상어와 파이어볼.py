''' 2차 풀이
[0] 타임라인
구상 (10분)
구현 (20분)
디버깅 (5분)

[1] 실수한점
1. value 자체가 리스트인데 new_atom[key]=[value] 리스트를 한번 더 감쌌음
-> 리스트 한번 더 / 덜 씌우는 실수 종종함, print해서 눈으로 확인하기, 체크리스트 추가하기

[2] 배운점

'''

# 격자의 크기, 원자의 개수, 실험 시간
N,M,K=map(int,input().split())
dic={0:(-1,0),1:(-1,1),2:(0,1),3:(1,1),4:(1,0),5:(1,-1),6:(0,-1),7:(-1,-1)}
atom={}

for _ in range(M):
    x,y,m,s,d=map(int,input().split())
    x,y=x-1,y-1
    atom[(x,y)]=[(m,s,d)]

# =======================

for _ in range(K):
    new_atom={}
    print(atom)
    for key,value in atom.items():
        si,sj=key
        for m,s,d in value:
            di,dj=dic[d]
            ni,nj=(si+di*s)%N,(sj+dj*s)%N

            if (ni,nj) in new_atom:
                new_atom[(ni,nj)].append((m,s,d))
            else:
                new_atom[(ni,nj)]=[(m,s,d)]
    atom=new_atom
    new_atom={}
    for key,value in atom.items():
        if len(value)>=2:
            sm_m=0     # 질량 합
            sm_s=0     # 속력 합
            cnt_d=0
            for m,s,d in value:
                sm_m+=m
                sm_s+=s
                if d in (0,2,4,6):
                    cnt_d+=1
            new_m=sm_m//5
            new_s=sm_s//len(value)
            if new_m!= 0:
                if cnt_d==len(value) or cnt_d==0:
                    new_atom[key]=[(new_m,new_s,0),(new_m,new_s,2),(new_m,new_s,4),(new_m,new_s,6)]
                else:
                    new_atom[key]=[(new_m,new_s, 1), (new_m,new_s, 3),(new_m,new_s, 5), (new_m,new_s, 7)]

        else:
            new_atom[key]=value
    print(new_atom)
    atom=new_atom

ans=0
for key,value in atom.items():
    for m,s,d in value:
        ans+=m

print(ans)

''''
마법사 상어와 파이어볼 (2/) / 2025-03-04 / 체감 난이도 : 골드 4
소요 시간 : 4시간..? / 시도 : 2회 / 실행 시간 : 268ms / 메모리 : 132976KB

[배운점 !!!!]
0) 도넛 행성처럼 모든 행과 열의 끝과 끝이 연결될 때는 그냥 %N 를 하기만 하면 된다
new_r=(r+dr[d][0]*s)%N
new_c=(c+dr[d][1]*s)%N

즉, 아래처럼 할 필요가 없음
if ni<0:
    ni=N-(abs(ni)%N)
elif ni>=N:
    ni=ni%N
if nj<0:
    nj=N-(abs(nj) % N)
elif nj>=N:
    nj=nj%N

이걸 이해하려면 음수일때 % 연산이 어떻게 되는지 알아야 하는데,
-1%3 을 1%3 으로 생각하고 N에서 빼준다고 생각하면 됨 3-1%3

1) 이전에 나는 리스트만 고집했었다 구상할 때 자료구조를 생각하고 들어가라는 스터디원들의 이야기를 제대로 실천하지 않았던 것 같다
-> set과 dictionary를 잘 활용하자
둘다 조회를 할 때 O(1)이기 때문에 조회시 유리하다
리스트에서 특정 원소를 조회할 때는, 리스트 안 원소의 개수를 K라고 할 때 O(K)만큼 시간이 걸린다

2) 리스트를 인덱스로 접근하면 그 인덱스에 있는 값들을 바꿔치기할 수 있다
for num in arr: 이런식으로 접근 할 때 num을 다른 숫자로 바꾸고 싶어서 num=다른 숫자, 했는데 반영이 안 되는 걸 보고
리스트의 특정 값을 중간에 바꿀 수 없다고 이상한 착각을 했다
그래서 popleft로 모든 원소를 다 빼주고 다시 append로 넣어주는 걸 반복했는데 .. 인덱스로 접근하면 가능하다 지금이라도 바로잡을 수 있어서 다행이다


3) 이 문제를 처음 풀 때 리스트를 돌면서 특정 값을 지우면 인덱스가 바뀌는데.. 이걸 도대체 어떻게 관리할지에 대한 방법이 안 떠올랐다
-> 해결 방법은 그냥 임시 리스트를 만들어서 원하는 원소만 넣고 그 전체를 다시 재할당 해주면 된다 ..

4) 아래와 같이 써서 튜플로는 append가 안 된다는 오류를 x10번쯤 봤다
new_fireball={}
for (r,c),(m,s,d) in fireball.items():
    ...
    if (new_r,new_c) in new_fireball:
        new_fireball[(new_r, new_c)].append((m, s, d))
    else:
        new_fireball[(new_r,new_c)]=(m,s,d)

-> 이렇게 리스트로 감싸줬어야 한다
    if (x,y) in new_fireball:
        new_fireball[(x,y)].append((sm_m,sm_s,odd[i]))
    else:
        new_fireball[(x,y)]=[(sm_m,sm_s,odd[i])]

5) 딕셔너리는 키를 수정할 수 없어서 .. 이럴 때도 새로운 딕셔너리에 수정된 키로 구성된 값들을 넣고 재할당 해주면 된다

[타임라인]
1. 문제 이해 & 구상 (10분) <- 1번 시간이 적을수록 망하는 길에 가까워지는 것 같다 ..
2. 구현 & 디버깅 (1시간 50분) <- 도대체 내가 이 많은 시간을 어떻게 흘려보낸건지 ..
구상 제대로 안한 채 코드 쓰고 고치고 디버깅을 반복하다 보니 이렇게 된 것 같다

[디버깅 내역]
- 같은 변수를 여러번 써서 값이 이상하게 할당됐다
- ni,nj를 ni,ni로 적었다
- 배열에서 원소를 삭제할 때 인덱스 바껴서 안 된다는 오류 x10번 마주했다
- 고친다고 고쳤는데 결국 제대로 안 나와서 오픈 테케의 정답이 다르게 나왔다
- 다 돌아가긴 하지만, 오픈 테케와 정답이 안 맞을 때 디버깅도 엉망이였다
예제를 보면서 디버깅을 할 거면 예제를 먼저 완벽히 예측하고 시작하자
예측하고 비교하고 예측하고 비교하고 하니까 헷갈려서 몇번을 왔다갔다 본건지?
그리고 무작정 디버깅을 시작하기 전에 오타가 있는지 맥락이 맞는지 한 번 훑어보고 하자
디버깅 냅다 시작했는데 알고보니 오타 때문이였다면.. 시간 낭비를 하는 것이다

[구상]
딕셔너리로 (좌표) : (질량,속도,방향)

[구현]

[마지막 체크 포인트]

[후기]
배운게 많은 문제, 초반 시간을 어떻게 보내는지가 정말 중요하다
구현 하다가 산으로 가고 있을 때는 (구상을 제대로 안 하고 덤볐을 때는) 중단하고 구상으로 다시 돌아가야 함
그리고 아직 딕셔너리를 잘 못 쓰는 것 같다 연습하자 !


조회를 하냐 순회 하냐 구분을 하자 !!!
조회를 많이 할 때는 set이나 딕셔너리가 유리하고
순회할 때는 배열이 낫다 !!!
모든 값을 다 볼 때는 리스트가 낫다

근데 마지막에서 빼고 넣고가 많이 나오면 덱을 고려해봐야한다
근데 특정 인덱스를 뽑을 때는 덱이 너무 느림

삽입과 삭제가 자주 일어난다 -> 덱 고려
특정 인덱스를 뽑아올 때는 -> 리스트 고려
덱도 pop(i)가 되기는 하는데 느림 !!!

== 할 때 하나씩 다 보니까 오래 걸리니까 중요한 건 개수니까 cnt로 해주면 되지 않을까?
'''

dr={0:(-1,0), 1: (-1,1), 2: (0,1), 3: (1,1), 4: (1,0), 5: (1,-1), 6: (0,-1), 7: (-1,-1)}

#격자 크기, 파이어볼 개수, 명령 횟수
N,M,K=map(int,input().split())
fireball={}

# 초기 파이어볼에 추가
for _ in range(M):
    r,c,m,s,d=map(int,input().split())
    r,c=r-1,c-1
    fireball[(r,c)]=[(m,s,d)]


cnt=0
while cnt<K:
    # 한 번 한 거 체크
    cnt+=1

    # 모든 파이어 볼이 이동
    # 딕셔너리는 키를 수정할 수 없어서 매번 새로운 거 만들어서 재할당 하는 수 밖에..
    new_fireball={}
    for (r,c),llst in fireball.items():
        for m,s,d in llst:
            new_r=(r+dr[d][0]*s)%N
            new_c=(c+dr[d][1]*s)%N
            if (new_r,new_c) in new_fireball:
                new_fireball[(new_r, new_c)].append((m, s, d))
            else:
                new_fireball[(new_r,new_c)]=[(m,s,d)]

    fireball=new_fireball

    new_fireball={}
    # 순회하면서 동시에 수정이 안 될 때? 새로운 임시 딕셔너리를 또 만들면 됨
    for item in fireball:
        x,y=item[0],item[1]
        if len(fireball[item])>=2:
            sm_m=0
            sm_s=0
            odd=[]
            for it in fireball[item]:
                sm_m+=it[0]
                sm_s+=it[1]
                odd.append(it[2]%2)

            sm_m=sm_m//5
            sm_s=sm_s//len(fireball[item])
            if odd==[0]*len(fireball[item]) or odd==[1]*len(fireball[item]):
                odd=[0,2,4,6]
            else:
                odd=[1,3,5,7]


            if sm_m !=0:
                for i in range(4):
                    if (x,y) in new_fireball:
                        new_fireball[(x,y)].append((sm_m,sm_s,odd[i]))
                    else:
                        new_fireball[(x,y)]=[(sm_m,sm_s,odd[i])]
        else:
            new_fireball[item]=fireball[item]

    fireball=new_fireball

ans=0
for lst in fireball.values():
    for val in lst:
        ans+=val[0]

print(ans)