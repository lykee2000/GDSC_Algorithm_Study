# BOJ 2164 카드2
from collections import deque
n = int(input())  # n장 카드 입력
card = deque([i for i in range(1, n+1)])
while len(card) > 1:  # card에 한장이 남을때 까지 반복
    card.popleft()  # 제일 위에있는 카드 버리기
    move = card.popleft()  # 그다음 제일 위에 잇는 카드를 move에 저장 후 버리기
    card.append(move)  # move를 제일 아래에 잇는 카드 밑으로 옮긴다.
print(card[0])  # 제일 마지막에 남게 된는 카드 출력
