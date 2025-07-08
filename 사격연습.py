# 보드 판의 크기 (2<= <=8)
N=int(input())

# 사격 횟수 K (1<= <=5)
K=int(input())

# NxN 크기의 보드 정보
# 표적의 위치 : 1 이상의 자연수 (초기 체력), 0 : 표적이 없는 곳
arr=[list(map(int,input().split())) for _ in range(N)]

# init[(i,j)]=초기체력, 보너스 표적이 아닌 것만 저장하기
init={}
for i in range(N):
    for j in range(N):
        if 1<=arr[i][j]<=9:
            init[(i,j)]=arr[i][j]

# 각 총알의 공격력
lst=list(map(int,input().split()))

# 각 위치마다 초기체력이 있다
# 1. 한번의 사격을 할 떄 1행부터 N행까지 중에서 하나의 행 선택하여 사격
# 총알은 가장 왼쪽에서 시작해 오른쪽으로 한 칸씩 이동하며 날아감
# 총알이 표적에 닿으면 현재 체력 - 총알의 공격력
# 표적에 닿으면 총알은 즉시 사라짐
# 현재 체력이 0 이하가 되면 표적은 사라지고, 표적의 초기 체력만큼 점수를 얻음
# 사라진 표적 위치의 상하좌우 위치 중에서 빈칸인 모든 위치에 대하여 초기 체력 // 4 의 값을 가지는 표적 생성
# 그 값이 0 이라면 새로운 표적 안 생김

# 값이 10 이상인 표적은 보너스 표적이고 이를 맞히는 순간 총알의 공격력과 상관없이
# 총알과 보너스 표적 함께 사라지고 ( 빼는 과정이 없음 ) 그 즉시 더함
# 사라진 뒤에 새로운 표적도 생성하지 않음

# i번째 행을 보고있다
# 초기 체력을 따로 기록해둬야함
# 딕셔너리에 저장?
# 없어지면 지우면 되니까

def simul(power,i,arr,init):
    result=0

    for j in range(N):
        if arr[i][j] == 0: continue
        elif arr[i][j]>=10:
            # 점수 더하고
            result=arr[i][j]
            # 바로 사라진다
            arr[i][j]=0
            return result

        # 일반 표적이면
        elif 1<=arr[i][j]<=9:
            arr[i][j]-=power
            if arr[i][j]<=0:
                arr[i][j]=0
                result=init[(i,j)]
                del init[(i,j)]
                for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                    ni,nj=i+di,j+dj
                    if not (0<=ni<N and 0<=nj<N) or arr[ni][nj] != 0: continue
                    init[(ni,nj)]=1
                    arr[ni][nj]=1
                    return result
    return result


# 메모리 주소 id를 보낸다고 생각해야함
# 현재 idx 총알을 사용하고 있고, 현재 상태의 맵이 arr, 점수
def btk(idx,arr,init,mx):
    global ans

    if idx == len(lst):
        ans=max(ans,mx)
        return

    for i in range(N):
        temp=[row[:] for row in arr]
        result=simul(lst[idx],i,arr,init)
        btk(idx+1,arr,init,mx+result)

ans=0
# 매번 행 중 어떤 행을 갈 건지 선택하는 백트래킹임
btk(0,arr,init,0)

# 출력
# K번 사격이 가능할 때 얻을 수 있는 최대 점수 출력하기
print(ans)