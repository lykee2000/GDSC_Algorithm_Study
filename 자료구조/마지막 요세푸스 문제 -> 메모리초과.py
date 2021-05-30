# BOJ 1179 마지막 요세푸스 문제
# 메모리초과
n, k = map(int, input().split())
arr = [i for i in range(1, n+1)]  # 1부터 N번까지 N명의 사람이 원을 이루면서 앉아있음
ans = []  # 제거된 사람들을 넣을 배열
num = 0  # 제거될 사람의 인덱스 번호

for j in range(n):
    num += k-1
    if num >= len(arr):  # 한바퀴를 돌고 그다음으로 돌아올때를 대비해 값을 나머지로 바꿈
        num = num % len(arr)
    ans.append(str(arr.pop(num)))

print(ans[-1])
