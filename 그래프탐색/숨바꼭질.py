# BOJ 1697 숨바꼭질
from collections import deque


def bfs():
    q = deque()
    q.append(n)  # 수빈이가 있는 위치 n 출발점 넣어줌
    while q:
        x = q.popleft()  # 제일 왼쪽 값 pop해서 x에 저장
        if x == k:  # x가 동생이 있ㄴ느 위치 k와 같을때
            return visit[x]  # visit[x]를 출력
        for i in [x-1, x+1, x*2]:  # x-1 x+1 x*2의 값을 i에 순서대로 넣어줌
            # i값이 0과 MAX 사이의 값이고 visit[i]가 0의 값을 가지면
            if 0 <= i < MAX and visit[i] == 0:
                visit[i] = visit[x] + 1  # visit[x] + 1을 해주고
                q.append(i)  # i를 추가


n, k = map(int, input().split())
MAX = 100001
visit = [0] * MAX
print(bfs())
