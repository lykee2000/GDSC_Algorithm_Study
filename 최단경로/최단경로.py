# BOJ 1753 최단경로
import sys
from heapq import heappush, heappop
inf = 100000000
v, e = map(int, sys.stdin.readline().split())  # v은 노드(정점)개수, e은 에지 개수
k = int(sys.stdin.readline())  # 시작점
s = [[] for _ in range(v + 1)]
dp = [inf] * (v + 1)
heap = []


def dijkstra(start):
    # 0번 노드에서 다른 모든 노드 까지의 최단 경로의 길이를 리스트dist 에 저장
    dp[start] = 0  # 소스노드는 0번노드
    # 우선순위 힙 생성 _ 시작 노드로 가기 위한 최단경로를 0으로 설정 후 큐에 삽입
    heappush(heap, [0, start])
    while heap:
        w, n = heappop(heap)  # 원소 꺼내기
        for n_n, wei in s[n]:
            n_w = wei + w
            if n_w < dp[n_n]:  # 값 비교해서 더 작은 값을 더 짧은 경로로 dist 갱신
                dp[n_n] = n_w
                heappush(heap, [n_w, n_n])


for i in range(e):
    u, v, w = map(int, sys.stdin.readline().split())  # 가중치 w를 갖는 에지(u,v) 입력
    s[u].append([v, w])  # u노드에서 v노드까지 가는 가중치 w 저장
dijkstra(k)
# 시작 노드로 부터 갈 수 없는 경우 INF 출력
for i in dp[1:]:
    print(i if i != inf else "INF")
