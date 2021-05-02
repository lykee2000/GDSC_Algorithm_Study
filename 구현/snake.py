# BOJ_3190뱀
def change(d, c):
    if c == "L":  # 왼쪽 회전
        d = (d - 1) % 4
    else:  # 동쪽 회전
        d = (d + 1) % 4
    return d


# 상 우 하 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def start():
    direction = 1  # 초기 방향
    time = 1  # 시간
    y, x = 0, 0  # 초기 뱀 위치
    visited = deque([[y, x]])  # 방문 위치
    board[y][x] = 2
    while True:
        y, x = y + dy[direction], x + dx[direction]
        if 0 <= y < N and 0 <= x < N and board[y][x] != 2:
            if not board[y][x] == 1:  # 사과가 없는 경우
                temp_y, temp_x = visited.popleft()
                board[temp_y][temp_x] = 0  # 꼬리 제거
            board[y][x] = 2
            visited.append([y, x])
            if time in snake.keys():
                direction = change(direction, snake[time])
            time += 1
        else:  # 본인 몸에 부딪히거나, 벽에 부딪힌 경우
            return time


N = int(input())  # 보드의 크기 n*n
K = int(input())  # 사과의 개수

board = [[0] * N for _ in range(N)]  # 사과 위치 저장할 리스트

for _ in range(K):
    r, c = map(int, input().split())  # 사과 위치 입력받기
    board[r-1][c-1] = 1  # 사과가 있는 위치는 1

L = int(input())  # 뱀의 방향 변환 횟수
snake = {}

for _ in range(L):
    X, C = input().split()
    snake[int(X)] = C  # 뱀의 방향 변환 정보 입력받기
print(start())
