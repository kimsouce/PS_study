str_1 = input()
str_2 = input() 

LCS = [[0] * (len(str_2)+1) for _ in range(len(str_1)+1)]  #맵 초기화  #가장 앞에 0

for i in range(1, len(str_1)+1):
  for j in range(1, len(str_2)+1):
    if str_1[i-1] == str_2[j-1]:
      LCS[i][j] = LCS[i-1][j-1] +1
    else:
      LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

print(LCS[-1][-1])
