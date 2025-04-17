N, M = map(int, input().split())
store = int(input())
store_spot = [list(map(int, input().split())) for _ in range(store)]
dong_spot = list(map(int, input().split()))


result = 1000
result_sum = 0

for i, j in store_spot:
    if i == 1 :
        if dong_spot[0] == i :
            result = min(result, abs(dong_spot[1] - j))
            result_sum += result
        elif dong_spot[0] == 2 :
            result = min(result, abs(N-dong_spot[1]) + M + N-j, dong_spot[1] + M + j)
            result_sum += result
        elif dong_spot[0] == 3:
            result = min(result, dong_spot[1] + j)
            result_sum += result
        elif dong_spot[0] == 4:
            result = min(result, dong_spot[1] + N-j)
            result_sum += result

    elif i == 2 :
        if dong_spot[0] == i :
            result = min(result, abs(dong_spot[1] - j))
            result_sum += result
        elif dong_spot[0] == 1 :
            result = min(result, abs(N-dong_spot[1]) + M + N-j, dong_spot[1] + M + j)
            result_sum += result
        elif dong_spot[0] == 3:
            result = min(result, dong_spot[1] + N-j)
            result_sum += result
        elif dong_spot[0] == 4:
            result = min(result, dong_spot[1] + N-j)
            result_sum += result

    elif i == 3 :
        if dong_spot[0] == i :
            result = min(result, abs(dong_spot[1] - j))
            result_sum += result
        elif dong_spot[0] == 1 :
            result = min(result, dong_spot[1] + j)
            result_sum += result
        elif dong_spot[0] == 2:
            result = min(result, dong_spot[1] + M-j)
            result_sum += result
        elif dong_spot[0] == 4:
            result = min(result, abs(M-dong_spot[1]) + N + M-j, dong_spot[1] + N + j)
            result_sum += result

    elif i == 4 :
        if dong_spot[0] == i :
            result = min(result, abs(dong_spot[1] - j))
            result_sum += result
        elif dong_spot[0] == 1 :
            result = min(result, N-dong_spot[1] + j)
            result_sum += result
        elif dong_spot[0] == 2:
            result = min(result, N-dong_spot[1] + M-j)
            result_sum += result
        elif dong_spot[0] == 3:
            result = min(result, abs(M-dong_spot[1]) + N + M-j, dong_spot[1] + N + j)
            result_sum += result

    result = 1000

print(result_sum)


