'''
B19238 스타트택시 / 2025-03-14 / 체감 난이도 : 골드 3
소요 시간 : 3시간 30분 / 시도 : 3회

[0] 총평
- 아기 상어랑 똑같이 거리마다 bfs를 돌려야하는 문제네
- 오픈테케 3번이 택시기사가 있는 곳 - 출발지까지 아예 갈 수가 없는 경우를 의미했지만,
처음에 이를 고려하지 못해서 오픈테케에서 틀림 -> 그렇다면 출발지 - 도착지까지도 못갈 수 있지 않을까? 라는 생각을 했어야 함
항상 의심 !

[1] 타임라인
1. 문제 이해 & 구상 & sudo code 작성 (20분)

2. 구현 (35분)
-> 오픈 테케 3번에서 index error 왜냐하면 lst에 아무것도 들어가지 않을 수 있으니까
-> 바로 찾고 제출했지만 실패, 이와 같은 맥락의 반례를 찾지 못함

3. 디버깅 (2시간)

[2] 배운점 및 실수한 점
- 디버깅을 2시간이나 했지만 못 찾음
1. 일단 화장실 다녀오고
2. 문제 다시 읽고 오타 있는지 확인, 찍어보면서 내가 생각한대로 연료가 반영이 되는지 확인 (1시간)
-> 이 과정을 통해 이리저리 많이 생각해봤다고 생각했지만 날카롭지 못했음
3. 새로운 테케를 만들어 보려고 노력은 했지만 이미 의심하던 부분에 대한 엣지케이스만 만듦 (1시간)
오타 없고 문제 이해 잘못된 거 없고 내가 의심스러운 부분을 다 반영한 거 같으면 이제 다음 의심스러운 걸 생각해야하는데
자꾸 현재 의심스럽다고 생각하는 부분만 보고 그 부분만 테케 만들어서 찍어봄

-> 실패 요인 : 결국 내 코드에서 내 생각에서 벗어나지 못함
내가 생각하지 못하고 있는 부분이 없을까 계속해서 생각해봐야함
특히 3번 엣지케이스가 생각의 힌트가 될 수 있었는데.. 왜 더 나아간 생각을 하지 못했을까

엣지에는 뭐가 있을까 직접 써보고 거창한 테케 아니여도 꼭 만들어 봐야한다고 !!!!

----
의심가는 부분?
- 택시와 승객이 같은 위치에 서있으면 그 승객까지의 최단거리는 0
- 한 승객을 목적지로 이동시키면 그 승객 출발지 - 도착지에서 소모한 연료 양의 두 배가 충전
- 이동하는 도중에 연료가 바닥나면 이동에 실패
-> 출발지까지 가는데 부족, 출발지-도착지 가는데 부족
- 승객을 목적지로 이동시키고 나서 T=0이 되는 건 상관 없음
- 모든 출발지는 다르고 -> 모든 도착지도 다르다는 말은 없음
근데 출발지 기준으로 인덱스를 찾아서 pop 시켰으니까 문제 없음
- 각 손님의 출발지와 목적지는 다르다 -> 손님 데려다줄 때 거리가 0일 수는 없음

!! 출발지에서 도착지까지 무조건 간다는 보장도 없음 !!
3번 테케가 힌트가 되지 않을까? 출발지까지 못 갈 수도 있다는 걸 보여줬으니, 그럼 출발지에서 도착지까지도 못갈 수 있는 거 아닌가? 라는 생각을 해봤어야
항상 의심 .. 항상 가능한 건 없다늬까..
'''

from collections import deque

def calculate():
    global si,sj,T

    while len(start) != 0:
        dist = 0
        stop = -1
        q = deque([(si, sj, dist)])
        v = [[0] * N for _ in range(N)]
        v[si][sj] = 1
        lst = []

        # 이미 start에 있으면, 즉 택시 출발지 == 승객 있는 곳이면
        if (si, sj) in start:
            # 그렇다면 아래 큐에서 다음으로 갈 거 찾지 않아도 됨
            lst.append((si, sj))
        else:
            while q:
                ci, cj, dist = q.popleft()
                if dist == stop:
                    break
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ni, nj = ci + di, cj + dj
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0 and v[ni][nj] == 0:
                        q.append((ni, nj, dist + 1))
                        v[ni][nj] = 1
                        if (ni, nj) in start:
                            stop = dist + 1
                            lst.append((ni, nj))

        if not lst:
            return -1

        lst.sort()

        gi, gj = lst[0]
        T -= dist

        # 만약 최단 거리에 있는 손님을 찾으러 가는데에 중간에 끊기면 못하는 거
        # 근데 어차피 아래에서 걸리지 않나..?
        if T < 0:
            return -1
        # 손님이 정해졌으면 거기로 또 가야지
        dist = 0
        flag = False
        idx = start.index((gi, gj))
        start.pop(idx)
        ei, ej = end[idx]
        end.pop(idx)

        q = deque([(gi, gj, dist)])
        v = [[0] * N for _ in range(N)]
        v[gi][gj] = 1

        while q:
            ci, cj, dist = q.popleft()
            if (ci, cj) == (ei, ej):
                T -= dist
                flag = True
                if T < 0:
                    return -1
                T += 2 * dist
                si, sj = ei, ej
                break
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni, nj = ci + di, cj + dj
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0 and v[ni][nj] == 0:
                    q.append((ni, nj, dist + 1))
                    v[ni][nj] = 1

        if not flag:
            return -1
    return T

N,M,T=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]

si,sj=map(int,input().split())
si,sj=si-1,sj-1

start=[]
end=[]
for _ in range(M):
    x1,y1,x2,y2=map(int,input().split())
    x1,y1,x2,y2=x1-1,y1-1,x2-1,y2-1
    start.append((x1,y1))
    end.append((x2,y2))

ans=calculate()
print(ans)