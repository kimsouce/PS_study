s = input()
chk = []
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        chk.append(s[i])

chk.append(s[-1])  # len(s)를 통해 맨 마지막 원소가 들어가지 못하기 때문에 따로 더해줌
zero = chk.count("0")
one = chk.count("1")
print(chk)
print(min(zero, one))
