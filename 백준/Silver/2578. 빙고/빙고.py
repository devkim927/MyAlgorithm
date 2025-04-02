def bingo_check(bingo_pan):
    global bingo
    bingo = 0
    lx, ly, rx, ry = 0, 0, 0, 4

    for x in range(5):
        for y in range(5):
            if bingo_pan[x][y] != 'b':
                break
            if y == 4 and bingo_pan[x][y] == 'b':
                bingo += 1

    for y in range(5):
        for x in range(5):
            if bingo_pan[x][y] != 'b':
                break
            if x == 4 and bingo_pan[x][y] == 'b':
                bingo += 1

    for i in range(5):
        if bingo_pan[lx + i][ly + i] != 'b':
            break
        if i == 4 and bingo_pan[lx + i][ly + i] == 'b':
            bingo += 1

    for j in range(5):
        if bingo_pan[rx + j][ry - j] != 'b':
            break
        if j == 4 and bingo_pan[rx + j][ry - j] == 'b':
            bingo += 1


bingo_pan = [list(map(int, input().split())) for _ in range(5)]
call = []

for i in range(5):
    call_list = list(map(int, input().split()))
    for j in call_list:
        call.append(j)

call_cnt = 0
bingo = 0

for call_num in call:

    call_cnt += 1
    for x in range(5):
        for y in range(5):
            if bingo_pan[x][y] == call_num:
                bingo_pan[x][y] = 'b'
                break

    bingo_check(bingo_pan)
    if bingo >= 3:
        print(call_cnt)
        break