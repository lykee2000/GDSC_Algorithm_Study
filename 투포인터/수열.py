# BOJ 2559번 수열
n, k = map(int, input().split())  # 온도를 측정한 전체 날짜의 수와 합을 구하기 위한 연속적인 날짜의 수 입력받기
t = list(map(int, input().split()))  # 온도의 수열 n개 입력받기

sum = sum(t[:k])  # 맨 앞에서 k-1개 만큼의 합
max_sum = sum

for i in range(k, n):  # k번(index기준)째부터 맨 끝까지
    # 현재 자신(t[i])은 더하고 현재 자신으로부터 k번째 앞에 있는 수는 뺌 (t[i-k]) -> t[i]와 t[i-k] 사이 값들은 겹침.
    sum += t[i] - t[i-k]
    max_sum = max(max_sum, sum)  # 합이 최대가 되는 값
print(max_sum)
