N = int(input())
cardlist = [list(map(int, input().split())) for _ in range(N*2)]
result = []

now_a = [0] * 4
now_b = [0] * 4
for i in range(0, N*2, 2):
    for j in range(1, cardlist[i][0]+1):
        if cardlist[i][j] == 4:
            now_a[3] += 1
        elif cardlist[i][j] == 3:
            now_a[2] += 1
        elif cardlist[i][j] == 2:
            now_a[1] += 1
        elif cardlist[i][j] == 1:
            now_a[0] += 1
    for k in range(1, cardlist[i+1][0]+1):
        if cardlist[i+1][k] == 4:
            now_b[3] += 1
        elif cardlist[i+1][k] == 3:
            now_b[2] += 1
        elif cardlist[i+1][k] == 2:
            now_b[1] += 1
        elif cardlist[i+1][k] == 1:
            now_b[0] += 1

    if now_a[3] > now_b[3] :
        print('A')
        now_a = [0] * 4
        now_b = [0] * 4
    elif now_b[3] > now_a[3] :
        print('B')
        now_a = [0] * 4
        now_b = [0] * 4
    else:
        if now_a[2] > now_b[2]:
            print('A')
        elif now_b[2] > now_a[2]:
            print('B')
        else:
            if now_a[1] > now_b[1]:
                print('A')
            elif now_b[1] > now_a[1]:
                print('B')
            else:
                if now_a[0] > now_b[0]:
                    print('A')
                elif now_b[0] > now_a[0]:
                    print('B')
                else:
                    print('D')

        now_a = [0] * 4
        now_b = [0] * 4
