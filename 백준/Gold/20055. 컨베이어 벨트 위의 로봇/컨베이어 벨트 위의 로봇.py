N, K = map(int, input().split())
HP = list(map(int, input().split()))
robots = [False] * N

cnt = 0

while True:
    cnt += 1

    HP = [HP[-1]] + HP[:-1]
    robots = [False] + robots[:-1]
    robots[-1] = False


    for i in range(N - 2, -1, -1):
        if robots[i] and not robots[i + 1] and HP[i + 1] > 0:
            robots[i] = False
            robots[i + 1] = True
            HP[i + 1] -= 1
    robots[-1] = False


    if HP[0] > 0 and not robots[0]:
        robots[0] = True
        HP[0] -= 1

    if HP.count(0) >= K:
        print(cnt)
        break
