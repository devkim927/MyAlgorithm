from itertools import combinations

N = int(input())
taste = [list(map(int, input().split())) for _ in range(N)]

result = 99999

for r in range(1, N + 1):
    for combo in combinations(taste, r):
        S = 1
        B = 0
        for s, b in combo:
            S *= s
            B += b
        result = min(result, abs(S - B))

print(result)