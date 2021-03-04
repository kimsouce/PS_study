s = input()

cnt0 = 0 #전부 0으로 바꾸는 경우
cnt1 = 0 #전부 1로 바꾸는 경우

#첫번째 원소부터 처리
if s[0] == '1':
    cnt0 += 1
else:
    cnt1 += 1
#두번째 원소부터 확인
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        #다음 수에서 1로 바뀌는 경우
        if s[i+1] == '1':
            cnt0 += 1
        #다음 수에서 0으로 바뀌는 경우
        else:
            cnt1 += 1

print(min(cnt1, cnt0))
