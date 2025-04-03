import sys
sys.setrecursionlimit(100000)

def dfs(x, y):
    global t, switch, visited
    visited[x][y] = True
    switch = True

    for dx, dy in dxy:
        xi = x + dx
        yj = y + dy

        if 0 <= xi < N and 0 <= yj < N:
            if grid[xi][yj] > t and visited[xi][yj] == False:
                dfs(xi, yj)


N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
top = 0
result = 0
visited = [([False] * N) for _ in range(N)]
switch = False

for i in range(N):
    for j in range(N):
        if top < grid[i][j]:
            top = grid[i][j]

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for t in range(top):
    top_result = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] > t and visited[i][j] == False:
                switch = True
                dfs(i, j)
                if switch:
                    top_result += 1
                    switch = False
    result = max(result, top_result)
    visited = [([False] * N) for _ in range(N)]

print(result)