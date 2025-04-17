N = int(input())
grid = [list(map(str, input().strip())) for _ in range(N)]
mobis = ['O', 'B', 'I', 'S']
cnt = 0

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

for i in range(N):
    for j in range(N):
        if grid[i][j] == 'M':
            for dx, dy in dxy:
                mi = i + dx
                mj = j + dy
                test = 'M'
                for m in range(4):
                    if 0 <= mi < N and 0 <= mj < N:
                        if grid[mi][mj] != mobis[m]:
                            break
                        else:
                            mi, mj = mi+dx, mj+dy
                            test += mobis[m]
                    if test == 'MOBIS':
                        cnt += 1
                        
print(cnt)