# 꼭짓점의 개수 (5000, 짝수)
N=int(input())
dot=[tuple(map(int,input().split())) for _ in range(N)]
M=int(input())
hole=[tuple(map(int,input().split())) for _ in range(M)]
print(dot)
print(hole)

point=[]
idx=0
for i in range(N):
    if dot[i] == [hole[idx][0],hole[idx][1]]:
        point.append(i)
        