# jungol_4189장기2_BFS
from collections import deque

n, m = map(int, input().split())  # 장기판 행의 수 n , 열의 수 m
# 말이 있는 위치의 행(R), 열(C)의 수/ 졸이 있는 위치의 행(S), 열(K)의 수
r, c, s, k = map(int, input().split())

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]


def bfs():
    cnt = 0
