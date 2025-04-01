def find_subsets(start, currunt_subset, acc):
    global cnt
    if acc > K:	                                    # 경우의 수를 줄이기 위해 K를 넘기는 경우는 계산 안 함
        return
    if acc == K:                                    # 만족하는 수가 되면 카운트
        cnt += 1
    for i in range(start, N):	                    # 시작인 0부터 N까지 돎
        num = k_list[i]
        currunt_subset.append(num)	                # 배열안에서 조합을 확인해보자
        find_subsets(i+1, currunt_subset, acc+num)  # acc에 선택한 수를 더해 합이 다름 재귀에서 합이 만족하는지를 확인
        currunt_subset.pop()                        # 조사하러 갔다가 다시 돌아오면 이번에 선택한 값 제거, 백트래킹의 핵심

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    k_list = list(map(int, input().split()))

    cnt = 0
    find_subsets(start=0, currunt_subset=[], acc=0)

    print(f"#{tc}", cnt)