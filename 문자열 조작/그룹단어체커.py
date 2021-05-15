# BOJ 1316번 그룹단어체커

n = int(input())  # 단어의 개수
num = n  # 그룹단어 개수
str = []
for i in range(n):
    s = input()
    for j in range(len(s)-1):
        if s[j] == s[j+1]:
            pass
        elif s[j] in s[j+1:]:  # 현재 위치 기준으로 뒷부분에 똑같은 문자가 나오면
            num -= 1  # 그룹단어가 아님
            break
print(num)
