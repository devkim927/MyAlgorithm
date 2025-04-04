N = int(input())
human = [list(map(int, input().split())) for _ in range(N)]
result = [0] * N

for i in range(N):
    idx = 1
    for j in range(N):
        if human[i][0] < human[j][0] and human[i][1] < human[j][1]:
            idx += 1

    result[i] = idx

for p in result:
    print(p, end=" ")
print()