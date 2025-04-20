N = int(input())

paper = [[0]*100 for _ in range(100)]

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y + 10):
            if paper[i][j] == 0:
                paper[i][j] = 1

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

cnt = 0

for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            for dx, dy in dxy:
                xi = i + dx
                yj = j + dy
                if 0 <= xi < 100 and 0 <= yj < 100 :
                    if paper[xi][yj] == 0:
                        cnt += 1
                elif xi < 0 or yj < 0 or xi == 100 or yj == 100:
                    cnt += 1

print(cnt)