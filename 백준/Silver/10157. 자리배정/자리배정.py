C, R = map(int, input().split())
K = int(input())

hall = [[0]*C for _ in range(R)]
i, j, start = R-1, 0, 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
d = 0

hall[i][j] = start
if K == 1 and C*R >= K:
    print(1, 1)
elif C*R >= K:
    while start <= K:
        nx = i + dx[d % 4]
        ny = j + dy[d % 4]
        if 0 <= nx < R and 0 <= ny < C and hall[nx][ny] == False:
            i, j = nx, ny
            hall[i][j] = start
            start += 1
        else:
            d += 1
        if start == K:
            print(j+1, R-i)
            start = K+1
            break
else:
    print(0)