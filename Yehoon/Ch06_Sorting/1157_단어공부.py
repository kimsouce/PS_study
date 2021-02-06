from collections import Counter
word = input().strip().upper()
char_cnt = Counter(word)
print(char_cnt)
common = char_cnt.most_common()
print(common)
if len(common) > 1 and int(common[0][1]) == int(common[1][1]):
    print("?")
else:
    print(common[0][0])

# 런타임 에러 코드
# a, b = char_cnt.most_common(2)
# if a[1] == b[1]:
#     print("?")
# else:
#     print(a[0])