# jungol_1695단지번호붙이기_DFS / BOJ 2667_DFS

def dfs(x, y, cnt):
    # 방향 이동 (위쪽 아래쪽 왼쪽 오른쪽)
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    graph[x][y] = 0  # 방문표시

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == '1':
            # 현재 단지에 속하는 집의 수 증가(cnt+1), 다음 집 탐색(nx,ny)
            cnt = dfs(nx, ny, cnt+1)
    return cnt  # 단지에 속하는 집의 수 반환


# n 입력받기
n = int(input())
graph = [list(input()) for _ in range(n)]  # n*n 크기의 지도를 입력받아 graph 배열 생성
cnt = 0
visit = []
# graph[i][j]가 1이면 dfs(i,j,1) 실행 -> 이어져 있는 집들을 다 세주면서 방문표시 0으로 해줌. visit배열에 각 단지별로 집의수 추가.
for i in range(n):
    for j in range(n):
        if graph[i][j] == '1':
            visit.append(dfs(i, j, 1))

print(len(visit))  # 총 단지 수 출력
for i in sorted(visit):  # 집의 수를 오름차순정렬 후 차례대로 출력
    print(i)
