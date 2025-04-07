def dfs(i, j):
    global cnt
    visited[i][j] = True
    for dx, dy in dxy:
        xi = i + dx
        yj = j + dy

        if 0 <= xi < h and 0 <= yj < w:
            if grid[xi][yj] == 1 and visited[xi][yj] == False:
                dfs(xi, yj)


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    grid = [list(map(int, input().split())) for _ in range(h)]
    visited = [([False] * w) for _ in range(h)]

    dxy = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 and visited[i][j] == False:
                cnt += 1
                dfs(i, j)

    print(cnt)