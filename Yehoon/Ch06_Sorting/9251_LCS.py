str_1 = input()
str_2 = input()
str_1, str_2 = str(0) + str_1, str(0) + str_2

# 2차원 리스트 0으로 초기화
result = [[0]*len(str_1)]*len(str_1)

# 두번째 문자가 행
for i in range(1, len(str_2)+1):
    list_2 = []
    cnt = 0
    #첫번째 문자가 열
    for j in range(1, len(str_1)+1):
        #첫번째 열은 0
        if j-1 == 0:
            list_2.append(cnt)

        # 위의 행의 숫자가 0이 아닐 땐, 그대로 내려옴
        elif str_1[j-1] != str_2[i-1] and result[i-2][j-1] > cnt:
            cnt += 1
            list_2.append(cnt)

        # 문자가 같을 때 count +1
        elif str_2[i-1] == str_1[j-1]:
            cnt += 1
            list_2.append(cnt)
        else:
            list_2.append(cnt)
    result[i-1] = (list_2)

print(result[-1][-1])