s = input().upper()

dic = {}
for i in range(len(s)):
    if s[i] not in dic:
        dic[s[i]] = 1
    else:
        dic[s[i]] += 1

s_dic = sorted(dic.items(), key=lambda x: x[1])

if len(s) == 1:
    print(s)
else:
    print('?' if s_dic[-1][1] == s_dic[-2][1] else s_dic[-1][0])
