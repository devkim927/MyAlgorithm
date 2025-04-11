N, H = map(int, input().split())
hunt = list(map(int, input().split()))

for i in range(len(hunt)):
    H = H - hunt[i]
    if H <= 0:
        print(i+1)
        break

if H > 0:
    print(-1)