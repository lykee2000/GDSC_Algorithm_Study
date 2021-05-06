# BOJ 1449번 수리공 항승 / 그리디

n, L = map(int, input().split())  # 물이 새는 곳의 개수 / 테이프의 길이
s = list(map(int, input().split()))  # 물이 새는 곳의 위치 저장 리스트
s.sort()  # 위치 오름차순 정렬

start = s[0]  # 시작지점
end = s[0] + L  # 시작지점에서 L길이를 더하기 -> 그 사이의 위치에는 모두 막을 수 있음.
cnt = 1

for i in range(n):
    if start <= s[i] < end:
        continue
    else:
        start = s[i]
        end = s[i] + L
        cnt += 1
print(cnt)
