N, M = map(int, input().split())  # N부터 M까지의 범위 받기
a = []  # 소수를 저장할 리스트

for i in range(N, M + 1):
    if i < 2:  # 2보다 작은 수는 소수가 아님
        continue
    is_prime = True  # 소수 여부를 판별하는 변수

    for j in range(2, int(i ** 0.5) + 1):  # 2부터 i의 제곱근까지 확인
        if i % j == 0:
            is_prime = False  # 나누어 떨어지면 소수가 아님
            break

    if is_prime:
        a.append(i)  # 소수라면 리스트에 추가

for s in a:
    print(s)
