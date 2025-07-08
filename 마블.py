# 보드 크기, 시작시 돈, 월급, 열쇠 개수
N,money,get,key=map(int,input().split())

# 마블 맵
marble=[0]*(4*N-4)
special=(0,N-1,2*N-2,3*N-3)

for idx in special:
    marble[idx]="S"

# 기부금
donate=0

key_info=[]
key_idx=0
for _ in range(key):
    x,y=map(int,input().split())
    key_info.append((x,y))

# 도시 구매했는지?
city=[0]*((4*N-8)-key)
city_info={}
city_idx=0

idx=1
for _ in range(4*N-8):
    if idx in special:
        idx+=1

    lst=input()

    if len(lst) == 1:
        marble[idx]="G"

    else:
        # 마블의 몇번째에 있는 도시가 city 리스트에 몇번째에 있는지
        city_info[idx]=city_idx
        marble[idx]=int(lst[2:])
        city_idx+=1

    idx+=1

# =========================================================================
# 여기서 시작 !
peop_idx=0
I=int(input())
locked=0


def my_print():
    print('---')
    print(marble)
    print(f'{turn}번 주사위 : {dice1} + {dice2} = {dice1 + dice2}')
    print(f'도착 인덱스와 행동 : {peop_idx}, {marble[peop_idx]}')

    if marble[peop_idx] == "G":
        print('뽑고 난 후 다음 황금 열쇠 인덱스, x번 행동, y만큼 :', key_idx, x, y)
    else:
        print(f' 땅 구매 현황 :', city)
    if locked > 0:
        print(f'만약 무인도에 있다면 남은 턴 수 : {locked}')

    print(f'수행 후 내 돈 : {money}')
    print(f'수행 후 기금 : {donate}')

def solve():

    global money,donate,key_idx,city_idx,peop_idx,locked

    if marble[peop_idx] == "S":
        if peop_idx == N-1:
            locked=4

        elif peop_idx == 2*N-2:
            money+=donate
            donate=0

        else:
            peop_idx=0
            money+=get

    elif marble[peop_idx] == "G":
        x,y=key_info[key_idx]
        key_idx=(key_idx+1)%len(key_info)

        if x == 1:
            money+=y
        elif x == 2:
            if money-y<0:
                return -1
            else:
                money-=y
        elif x == 3:
            if money-y<0:
                return -1
            else:
                money-=y
                donate+=y
        else:
            money += get * ((peop_idx + y) // len(marble))
            peop_idx = (peop_idx + y) % len(marble)
            solve()

    else: # 일반 - 도시칸
        # 아직 그 도시를 산 적이 없을 때
        if city[city_info[peop_idx]] == 0 and money>=marble[peop_idx]:
            money-=marble[peop_idx]
            city[city_info[peop_idx]] = 1

    return 1

# ===============================================================
# main

for turn in range(I):
    dice1,dice2=map(int,input().split())
    if locked > 0:
        if dice1 != dice2:
            locked -= 1
        else:
            locked = 0
        continue

    money += get * ((peop_idx + (dice1 + dice2)) // len(marble))
    peop_idx = (peop_idx+(dice1+dice2))%len(marble)
    ans=solve()
    my_print()
    if ans == -1:
        print("LOSE")
        break
else:
    if sum(city) == (4*N-8)-key:
        print("WIN")
    else:
        print("LOSE")
