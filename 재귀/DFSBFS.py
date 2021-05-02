# BOJ 1260 DFS와 BFS
from collections import deque


def dfs(v):
    print(v, end=' ')
    visit[v] = 1  # 방문 표시

    for i in range(1, n+1):
        if visit[i] == 0 and graph[v][i] == 1:
            dfs(i)


def bfs(v):
    queue = [v]
    visit[v] = 0
    while (queue):
        v = queue[0]
        print(v, end=' ')
        del queue[0]
        for i in range(1, n+1):
            if visit[i] == 1 and graph[v][i] == 1:  # 방문 표시가 1인 경우는 위에 dfs에서 이미 방문표시 1로 바꿔줬기때문
                queue.append(i)
                visit[i] = 0


n, m, v = map(int, input().split())  # 정점의 개수 n 간선의 개수 m 시작정점번호 v
graph = [[0]*(n+1) for i in range(n+1)]
visit = [0]*(n+1)
for i in range(m):
    x, y = map(int, input().split())  # 두 정점의 번호 x,y
    # 방향없음(양방향)
    graph[x][y] = 1  # x노드에서 y노드까지 가는
    graph[y][x] = 1  # y노드에서 x노드까지 가는

dfs(v)
print()
bfs(v)
