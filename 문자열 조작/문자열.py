# BOJ 1120번 문자열

a, b = input().split()
b = list(b)
max_cnt = 0

while len(a) <= len(b):
    cnt = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            cnt += 1
    max_cnt = max(max_cnt, cnt)
    del b[0]
print(len(a) - max_cnt)
