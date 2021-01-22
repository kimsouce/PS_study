# 펠린드롬은 회문 - 거꾸로 읽어도 말이 되는 것
from collections import Counter
import sys

word = list(map(str, input().upper()))

# 알파벳 이외 제거
only_char = []
for i in word:
    if i.isalpha():
        only_char.append(i)

# 홀수 개인 문자가 2개 이상일 때 펠린드롬 만들 수 없음
cnt_char = Counter(only_char)
odd, even = 0, 0
for i in cnt_char.values():
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
if odd > 1:
    print("I'm Sorry Hansoo")
    sys.exit()

# 펠린드롬 만들기
cnt_char = sorted(cnt_char.items(), key=lambda x:x[0])
palindrome = ""
if len(word)%2 == 0:
    for i in cnt_char:
        char = i[0]
        cnt = i[1]
        palindrome += char * (cnt//2)
    palindrome = palindrome + palindrome[::-1]
else:
    for i in cnt_char:
        char = i[0]
        cnt = i[1]
        palindrome += char * (cnt//2)
        if cnt%2 == 1:
            odd_char = char
    palindrome = palindrome + odd_char + palindrome[::-1]

print(palindrome)