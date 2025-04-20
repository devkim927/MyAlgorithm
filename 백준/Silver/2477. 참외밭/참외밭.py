K = int(input())
box = [list(map(int, input().split())) for _ in range(6)]

big = 0
small = 0

for i in range(6):
    d1, l1 = box[i]
    d2, l2 = box[(i + 1) % 6]

    test = l1 * l2
    if big < test:
        big = test
        small = box[(i + 3) % 6][1] * box[(i + 4) % 6][1]

print((big - small) * K)