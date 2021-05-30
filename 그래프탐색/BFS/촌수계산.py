# BOJ 2644 촌수계산
from collections import deque


def BFS(A, visited):
    queue = deque()
    # queue에 정점과 cnt 넣어주기
    queue.append((A, 0))
    visited[A] = True

    while queue:
        now, cnt = queue.popleft()
        # 정점이 B와 같으면 cnt 반환
        if now == B:
            return cnt

        for i in graph[now]:
            if visited[i] is False:
                # 해당 정점과 연결된 정점들 중에 방문 안한 정점이 있으면 queue에 추가
                queue.append((i, cnt + 1))
                # 방문 안한 정점이면 방문해주기
                visited[i] = True
    # 해당 정점과 연결된 모든 정점을 확인 했는데 B를 찾지 못했으면 연결되지 않았으므로 촌수를 계산할 수 없음
    return -1


# 전체 사람의 수 n, 우리가 촌수를 구해야 하는 사람 A, B
# 부모 자식간의 관계 개수 m
n = int(input())
A, B = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    # C가 D의 부모임
    C, D = map(int, input().split())
    # 양방향으로 그래프에 추가해줌
    graph[C].append(D)
    graph[D].append(C)

result = BFS(A, visited)
print(result)
