# TIL: 섬의 개수를 세는 문제 풀이
### 문제 분석
여러 개의 테스트 케이스가 주어짐.
각 테스트 케이스는 두 개의 정수 w(가로 크기)와 h(세로 크기)가 주어지고, 그 다음에 h줄에 걸쳐 w개의 정수로 이루어진 지도(0: 바다, 1: 땅)가 주어진다.
1인 곳이 섬이고, 연결된 1들이 하나의 섬을 이룬다.
섬은 가로, 세로뿐만 아니라 대각선으로도 연결될 수 있기 때문에 8방향 탐색을 해야 한다.

### 접근 방법
DFS (깊이 우선 탐색):
dfs(i, j) 함수는 주어진 좌표 (i, j)에서 시작하여, 8방향으로 연결된 1을 모두 방문하면서 하나의 섬을 탐색하는 함수입니다.
섬을 하나씩 찾을 때마다 cnt를 증가시켜 섬의 개수를 셈.

방문 체크:
각 칸을 방문했는지 확인하기 위해 visited 배열을 사용하여 중복 방문을 방지.

8방향 탐색:
8방향으로 연결된 1을 탐색해야 하므로, dxy 리스트에 (0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)을 설정.

종료 조건:
입력이 0 0일 경우 종료


```py
def dfs(i, j):
    global cnt
    visited[i][j] = True
    for dx, dy in dxy:
        xi = i + dx
        yj = j + dy

        if 0 <= xi < h and 0 <= yj < w:
            if grid[xi][yj] == 1 and visited[xi][yj] == False:
                dfs(xi, yj)


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    grid = [list(map(int, input().split())) for _ in range(h)]
    visited = [([False] * w) for _ in range(h)]

    dxy = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 and visited[i][j] == False:
                cnt += 1
                dfs(i, j)

    print(cnt)
```


# [Silver II] 섬의 개수 - 4963 

[문제 링크](https://www.acmicpc.net/problem/4963) 

### 성능 요약

메모리: 113416 KB, 시간: 168 ms

### 분류

그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

### 제출 일자

2025년 4월 8일 08:50:28

### 문제 설명

<p>정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.</p>

<p><img alt="" src="https://www.acmicpc.net/upload/images/island.png" style="width: 283px; height: 141px;"></p>

<p>한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다. </p>

<p>두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.</p>

### 입력 

 <p>입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다. w와 h는 50보다 작거나 같은 양의 정수이다.</p>

<p>둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.</p>

<p>입력의 마지막 줄에는 0이 두 개 주어진다.</p>

### 출력 

 <p>각 테스트 케이스에 대해서, 섬의 개수를 출력한다.</p>

