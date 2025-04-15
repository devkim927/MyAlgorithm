N = int(input())
M = int(input())
start = N*N
grid = [[False]*N for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
i, j, dr = 0, 0, 0

M_spot = [0, 0]

grid[i][j] = start
start -= 1
if grid[i][j] == M:
    M_spot[0], M_spot[1] = i+1, j+1

while start > 0:
    ni, nj = i+dx[dr], j+dy[dr]
    if 0 <= ni < N and 0 <= nj < N and grid[ni][nj] == False:
        i, j = ni, nj
        grid[i][j] = start
        start -= 1
    else:
        dr = (dr+1)%4
    if grid[i][j] == M:
        M_spot[0], M_spot[1] = i+1, j+1
        
for i in grid:
    print(*i)
print(*M_spot)