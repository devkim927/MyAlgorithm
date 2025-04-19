N = int(input())
cnt = 0
grid = [0 for _ in range(1001)]
H_spot = [0, 0]
LH_list = [list(map(int, input().split())) for _ in range(N)]

for l, h in LH_list:
    if h >= H_spot[1]:
        H_spot[0] = l
        H_spot[1] = h

grid[H_spot[0]] = H_spot[1]

for l, h in LH_list:
    if l < H_spot[0]:
        for j in range(l, H_spot[0]):
            if grid[j] < h:
                grid[j] = h

    elif l > H_spot[0]:
        for j in range(l, H_spot[0], -1):
            if grid[j] < h:
                grid[j] = h

print(sum(grid))
