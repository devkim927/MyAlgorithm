N, K = map(int, input().split())
cnt = 0
g_room = [0, 0, 0, 0, 0, 0, 0]
b_room = [0, 0, 0, 0, 0, 0, 0]
for i in range(N):
    S, Y = map(int, input().split())
    if S == 0:
        g_room[Y] += 1
    else:
        b_room[Y] += 1

for g in g_room:
    if 0 < g <= K:
        cnt += 1
    elif K < g and g % K != 0:
        cnt += g // K + 1
    elif g == 0:
        continue
    else:
        cnt += g // K

for b in b_room:
    if 0 < b <= K:
        cnt += 1
    elif K < b and b % K != 0:
        cnt += b // K + 1
    elif b == 0:
        continue
    else:
        cnt += b // K

print(cnt)