from collections import deque

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1

    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            xi = x + dx
            yj = y + dy

            if 0 <= xi < N and 0 <= yj < M:
                if miro[xi][yj] == 1 and visited[xi][yj] ==0:
                    visited[xi][yj] = 1 + visited[x][y]
                    q.append((xi, yj))

N, M = map(int, input().split())
miro = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

bfs(0, 0)

print(visited[N-1][M-1])