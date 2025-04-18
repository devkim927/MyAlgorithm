import sys
sys.setrecursionlimit(10000)

def eye(i, j, c):
    if grid[i][j] == c and visited[i][j] == False:              # 색상이 같은 것만 방문처리
        visited[i][j] = True
        for dx, dy in dxy:
            ni = i + dx
            nj = j + dy
            if 0 <= ni < N and 0 <= nj < N:
                eye(ni, nj, c)
    else:                                                       # 다른 색상은 탐색하지 않음
        return


def green_eye(i, j):                                            # 녹색, 적색을 동일하게 방문처리
    if grid[i][j] == 'R' and visited_green[i][j] == False:
        visited_green[i][j] = True
        for dx, dy in dxy:
            ni = i + dx
            nj = j + dy
            if 0 <= ni < N and 0 <= nj < N:
                green_eye(ni, nj)
    elif grid[i][j] == 'G' and visited_green[i][j] == False:    # 위와 동일한 방문리스트에 방문처리
        visited_green[i][j] = True
        for dx, dy in dxy:
            ni = i + dx
            nj = j + dy
            if 0 <= ni < N and 0 <= nj < N:
                green_eye(ni, nj)
    else:
        return

def green_eye_b(i, j):                                          # 적록인 경우 푸른색만 분리하여 방문처리
    if grid[i][j] == 'B' and visited_green[i][j] == False:
        visited_green[i][j] = True
        for dx, dy in dxy:
            ni = i + dx
            nj = j + dy
            if 0 <= ni < N and 0 <= nj < N:
                green_eye_b(ni, nj)
    else:
        return


N = int(input())
grid = [list(input().strip()) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
visited_green = [[False]*N for _ in range(N)]

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
eye_cnt = 0
green_eye_cnt = 0

for i in range(N):                      # 정상 안구
    for j in range(N):
        if visited[i][j] == False:      # 방문처리가 안된 곳을 방문처리 후 카운트
            eye(i, j, grid[i][j])
            eye_cnt += 1

for i in range(N):                      # 적록색약 안구
    for j in range(N):
        if grid[i][j] == 'R' and visited_green[i][j] == False:
            green_eye(i, j)
            green_eye_cnt += 1
        elif grid[i][j] == 'G' and visited_green[i][j] == False:
            green_eye(i, j)
            green_eye_cnt += 1
        elif grid[i][j] == 'B' and visited_green[i][j] == False:
            green_eye_b(i, j)
            green_eye_cnt += 1

print(eye_cnt, green_eye_cnt)