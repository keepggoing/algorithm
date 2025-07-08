'''
제 코드를 버리고 그냥 강사님 코드보고 다시 풀었삽니다..
처음 코드는 아래에 !
'''
T=int(input())

for _ in range(T):
    n=int(input())
    command=list(input().split())
    seq="ogwbry"
    c=[]

    # 자르기 쉽게 그냥 10개씩 넣는다구 생각
    for s in seq:
        for _ in range(10):
            c.append(s)

    for com in command:
        if com == 'U+':
            c[21:30] = c[27], c[24], c[21], c[28], c[25], c[22], c[29], c[26], c[23]
            c[7], c[8], c[9], c[31], c[34], c[37], c[43], c[42], c[41], c[19], c[16], c[13] = c[19], c[16], c[13], c[7],c[8], c[9], c[31], c[34], c[37], c[43], c[42], c[41]
        elif com == 'U-':
            c[21:30] = c[23], c[26], c[29], c[22], c[25], c[28], c[21], c[24], c[27]
            c[7], c[8], c[9], c[31], c[34], c[37], c[43], c[42], c[41], c[19], c[16], c[13] = c[31], c[34], c[37], c[43], c[42], c[41], c[19], c[16], c[13], c[7], c[8], c[9]
        elif com == 'D+':
            c[51:60] = c[57], c[54], c[51], c[58], c[55], c[52], c[59], c[56], c[53]
            c[3], c[2], c[1], c[11], c[14], c[17], c[47], c[48], c[49], c[39], c[36], c[33] = c[39], c[36], c[33], c[3],c[2], c[1], c[11], c[14], c[17], c[47], c[48], c[49]
        elif com == 'D-':
            c[51:60] = c[53], c[56], c[59], c[52], c[55], c[58], c[51], c[54], c[57]
            c[3], c[2], c[1], c[11], c[14], c[17], c[47], c[48], c[49], c[39], c[36], c[33] = c[11], c[14], c[17], c[47], c[48], c[49], c[39], c[36], c[33], c[3], c[2], c[1]

        elif com == 'F+':
            c[41:50] = c[47], c[44], c[41], c[48], c[45], c[42], c[49], c[46], c[43]
            c[17], c[18], c[19], c[27], c[28], c[29], c[37], c[38], c[39], c[57], c[58], c[59] = c[57], c[58], c[59], c[17],c[18], c[19], c[27], c[28], c[29], c[37], c[38], c[39]

        elif com == 'F-':
            c[41:50] = c[43], c[46], c[49], c[42], c[45], c[48], c[41], c[44], c[47]
            c[17], c[18], c[19], c[27], c[28], c[29], c[37], c[38], c[39], c[57], c[58], c[59] = c[27], c[28], c[29], c[37], c[38], c[39], c[57], c[58], c[59], c[17], c[18], c[19]

        elif com == 'B+':
            c[1:10] = c[7], c[4], c[1], c[8], c[5], c[2], c[9], c[6], c[3]
            c[11], c[12], c[13], c[21], c[22], c[23], c[31], c[32], c[33], c[51], c[52], c[53] = c[21], c[22], c[23], c[31], c[32], c[33], c[51], c[52], c[53], c[11], c[12], c[13]

        elif com == 'B-':
            c[1:10] = c[3], c[6], c[9], c[2], c[5], c[8], c[1], c[4], c[7]
            c[11], c[12], c[13], c[21], c[22], c[23], c[31], c[32], c[33], c[51], c[52], c[53] = c[51], c[52], c[53], c[11], c[12], c[13], c[21], c[22], c[23], c[31], c[32], c[33]

        elif com == 'L+':
            c[11:20] = c[17], c[14], c[11], c[18], c[15], c[12], c[19], c[16], c[13]
            c[1], c[4], c[7], c[21], c[24], c[27], c[41], c[44], c[47], c[59], c[56], c[53] = c[59], c[56], c[53], c[1], c[4], c[7], c[21], c[24], c[27], c[41], c[44], c[47]

        elif com == 'L-':
            c[11:20] = c[13], c[16], c[19], c[12], c[15], c[18], c[11], c[14], c[17]
            c[1], c[4], c[7], c[21], c[24], c[27], c[41], c[44], c[47], c[59], c[56], c[53] = c[21], c[24], c[27], c[41], c[44], c[47], c[59], c[56], c[53], c[1], c[4], c[7]

        elif com == 'R+':
            c[31:40] = c[37], c[34], c[31], c[38], c[35], c[32], c[39], c[36], c[33]
            c[3], c[6], c[9], c[23], c[26], c[29], c[43], c[46], c[49], c[57], c[54], c[51] = c[23], c[26], c[29], c[43], c[46], c[49], c[57], c[54], c[51], c[3], c[6], c[9]

        elif com == 'R-':
            c[31:40] = c[33], c[36], c[39], c[32], c[35], c[38], c[31], c[34], c[37]
            c[3], c[6], c[9], c[23], c[26], c[29], c[43], c[46], c[49], c[57], c[54], c[51] = c[57], c[54], c[51], c[3], c[6], c[9], c[23], c[26], c[29], c[43], c[46], c[49]

    for i in (21, 24, 27):
        print("".join(c[i:i + 3]))

'''
def rot(arr):
    return [list(row) for row in zip(*arr[::-1])]

def tor(arr):
    return [list(row) for row in zip(*arr)][::-1]

def up():
    global cube
    temp = [[lst[::] for lst in row] for row in cube]
    temp[0] = rot(cube[0])
    temp[1][0] = cube[2][0]
    temp[4][0] = cube[1][0][::-1]
    temp[3][0] = cube[4][0]
    temp[2][0] = cube[3][0]
    cube = [[lst[::] for lst in row] for row in temp]

def pu():
    global cube
    temp = [[lst[::] for lst in row] for row in cube]
    temp[0] = tor(cube[0])
    temp[2][0] = cube[1][0]
    temp[1][0] = cube[4][0][::-1]
    temp[4][0] = cube[3][0]
    temp[3][0] = cube[2][0]
    cube = [[lst[::] for lst in row] for row in temp]

def down():
    global cube
    temp = [[lst[::] for lst in row] for row in cube]
    temp[5] = rot(cube[5])
    temp[2][2] = cube[1][2]
    temp[1][2] = cube[4][2][::-1]
    temp[4][2] = cube[3][2]
    temp[3][2] = cube[2][2]
    cube = [[lst[::] for lst in row] for row in temp]

def nwod():
    global cube
    temp = [[lst[::] for lst in row] for row in cube]
    temp[5] = tor(cube[5])
    temp[1][2] = cube[2][2]
    temp[4][2] = cube[1][2][::-1]
    temp[3][2] = cube[4][2]
    temp[2][2] = cube[3][2]
    cube = [[lst[::] for lst in row] for row in temp]

def front():
    global cube
    tp = [[lst[::] for lst in row] for row in cube]
    tp[2]=rot(cube[2])
    tp[0][2][0], tp[0][2][1], tp[0][2][2] = cube[1][2][2], cube[1][1][2], cube[1][0][2]
    tp[1][2][2], tp[1][1][2], tp[1][0][2] = cube[5][2][2], cube[5][2][1], cube[5][2][0]
    tp[5][2][2], tp[5][2][1], tp[5][2][0] = cube[3][0][0], cube[3][1][0], cube[3][2][0]
    tp[3][0][0], tp[3][1][0], tp[3][2][0] = cube[0][2][0], cube[0][2][1], cube[0][2][2]
    cube = [[lst[::] for lst in row] for row in tp]

def tnorf():
    global cube
    tp = [[lst[::] for lst in row] for row in cube]
    tp[2] = tor(cube[2])
    tp[1][2][2], tp[1][1][2], tp[1][0][2] = cube[0][2][0], cube[0][2][1], cube[0][2][2]
    tp[5][2][2], tp[5][2][1], tp[5][2][0] = cube[1][2][2], cube[1][1][2], cube[1][0][2]
    tp[3][0][0], tp[3][1][0], tp[3][2][0] = cube[5][2][2], cube[5][2][1], cube[5][2][0]
    tp[0][2][0], tp[0][2][1], tp[0][2][2] = cube[3][0][0], cube[3][1][0], cube[3][2][0]
    cube = [[lst[::] for lst in row] for row in tp]

def back():
    global cube
    tp = [[lst[::] for lst in row] for row in cube]
    tp[4] = rot(cube[4])
    tp[1][2][0], tp[1][1][0], tp[1][0][0] = cube[0][0][0], cube[0][0][1], cube[0][0][2]
    tp[5][0][2], tp[5][0][1], tp[5][0][0] = cube[1][2][0], cube[1][1][0], cube[1][0][0]
    tp[3][0][2], tp[3][1][2], tp[3][2][2] = cube[5][0][2], cube[5][0][1], cube[5][0][0]
    tp[0][0][0], tp[0][0][1], tp[0][0][2] = cube[3][0][2], cube[3][1][2], cube[3][2][2]
    cube = [[lst[::] for lst in row] for row in tp]


def kcab():
    global cube
    tp = [[lst[::] for lst in row] for row in cube]
    tp[4] = tor(cube[4])
    tp[0][0][0], tp[0][0][1], tp[0][0][2] = cube[1][2][0], cube[1][1][0], cube[1][0][0]
    tp[1][2][0], tp[1][1][0], tp[1][0][0] = cube[5][0][2], cube[5][0][1], cube[5][0][0]
    tp[5][0][2], tp[5][0][1], tp[5][0][0] = cube[3][0][2], cube[3][1][2], cube[3][2][2]
    tp[3][0][2], tp[3][1][2], tp[3][2][2] = cube[0][0][0], cube[0][0][1], cube[0][0][2]
    cube = [[lst[::] for lst in row] for row in tp]


def left():
    global cube
    tp = [[lst[::] for lst in row] for row in cube]
    tp[1] = rot(cube[1])
    tp[0][2][0], tp[0][1][0], tp[0][0][0] = cube[4][0][2], cube[4][1][2], cube[4][2][2]
    tp[4][0][2], tp[4][1][2], tp[4][2][2] = cube[5][2][0], cube[5][1][0], cube[5][0][0]
    tp[5][2][0], tp[5][1][0], tp[5][0][0] = cube[2][2][0], cube[2][1][0], cube[2][0][0]
    tp[2][2][0], tp[2][1][0], tp[2][0][0] = cube[0][2][0], cube[0][1][0], cube[0][0][0]
    cube = [[lst[::] for lst in row] for row in tp]

def tfel():
    global cube
    tp = [[lst[::] for lst in row] for row in cube]
    tp[1] = tor(cube[1])
    tp[4][2][2], tp[4][1][2], tp[4][0][2] = cube[0][2][0], cube[0][1][0], cube[0][0][0]
    tp[5][2][0], tp[5][1][0], tp[5][0][0] = cube[4][0][2], cube[4][1][2], cube[4][2][2]
    tp[2][2][0], tp[2][1][0], tp[2][0][0] = cube[5][2][0], cube[5][1][0], cube[5][0][0]
    tp[0][2][0], tp[0][1][0], tp[0][0][0] = cube[2][2][0], cube[2][1][0], cube[2][0][0]
    cube = [[lst[::] for lst in row] for row in tp]

def right():
    global cube
    tp = [[lst[::] for lst in row] for row in cube]
    tp[3] = rot(cube[3])
    tp[4][0][0], tp[4][1][0], tp[4][2][0] = cube[0][2][2], cube[0][1][2], cube[0][0][2]
    tp[5][0][2], tp[5][1][2], tp[5][2][2] = cube[4][0][0], cube[4][1][0], cube[4][2][0]
    tp[2][2][2], tp[2][1][2], tp[2][0][2] = cube[5][0][2], cube[5][1][2], cube[5][2][2]
    tp[0][2][2], tp[0][1][2], tp[0][0][2] = cube[2][2][2], cube[2][1][2], cube[2][0][2]
    cube = [[lst[::] for lst in row] for row in tp]

def thgir():
    global cube
    tp = [[lst[::] for lst in row] for row in cube]
    tp[3] = tor(cube[3])
    tp[0][2][2], tp[0][1][2], tp[0][0][2] = cube[4][0][0], cube[4][1][0], cube[4][2][0]
    tp[4][0][0], tp[4][1][0], tp[4][2][0] = cube[5][0][2], cube[5][1][2], cube[5][2][2]
    tp[5][0][2], tp[5][1][2], tp[5][2][2] = cube[2][2][2], cube[2][1][2], cube[2][0][2]
    tp[2][2][2], tp[2][1][2], tp[2][0][2] = cube[0][2][2], cube[0][1][2], cube[0][0][2]
    cube = [[lst[::] for lst in row] for row in tp]


T=int(input())

for _ in range(T):
    cube = [[['w'] * 3 for _ in range(3)],
            [['g'] * 3 for _ in range(3)],
            [['r'] * 3 for _ in range(3)],
            [['b'] * 3 for _ in range(3)],
            [['o'] * 3 for _ in range(3)],
            [['y'] * 3 for _ in range(3)]]

    n=int(input())
    command=list(input().split())
    for com in command:
        if com == 'U+':
            up()
        elif com == 'U-':
            pu()
        elif com == 'D+':
            down()
        elif com == 'D-':
            nwod()
        elif com == 'F+':
            front()
        elif com == 'F-':
            tnorf()
        elif com == 'B+':
            back()
        elif com == 'B-':
            kcab()
        elif com == 'L+':
            left()
        elif com == 'L-':
            tfel()
        elif com == 'R+ ':
            right()
        elif com == 'R-':
            thgir()

        print(com)
        for row in cube:
            print(*row)
        print('---')
    for row in cube[0]:
        print("".join(row))
'''
