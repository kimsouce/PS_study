score = input()

length = len(score)
summ = 0

#왼쪽 부분 합
for i in range(length//2):
    summ += int(score[i])

#오른쪽 부분 합
for i in range(length//2,length):
    summ -= int(score[i])

if summ == 0:
    print('LUCKY')
else:
    print('READY')





#score_f = score[:mid]
#score_e = score[mid:]

#if sum(score_f) == sum(score_e):
#    print('LUCKY')
#else:
#    print('READY')

