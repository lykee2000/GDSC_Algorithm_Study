# 그리디 회의실배정 BOJ 1931번

n = int(input())
A = []
for i in range(n):
    a, b = map(int, input().split())
    # c = (a, b)  # 튜플형식
    A.append([a, b])
A = sorted(A, key=lambda a: a[0])  # 시작시간 기준 정렬
A = sorted(A, key=lambda a: a[1])  # 끝나는 시간 기준 정렬

k = 0
cnt = 0
for i in range(n):
    if A[i][0] >= k:
        cnt += 1
        k = A[i][1]
print(cnt)

# for i in range(0, n):
#     if A[i][0] >= A[k][1]:
#         cnt += 1
#         k = i
# print(cnt)
