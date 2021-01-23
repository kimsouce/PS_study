names = input()
chk_name = [0] * 26  # names에 들어온 알파벳을 저장하기 위한 리스트

# 알파벳 개수 세기
for n in names:
    chk_name[ord(n)-ord('A')] += 1  # 0 : A  ~ 25 : Z

cnt_odd = 0
odd_str = ''
palindrome_half = ''
for i in range(26):
    if chk_name[i] % 2 != 0:
        cnt_odd += 1
        odd_str += chr(i+65)
    # 짝수개인 알파벳을 odd_str기준으로 앞뒤로 붙여야하므로 2로 나눈 값의 몫만큼 대입
    palindrome_half += chr(i+65) * (chk_name[i] // 2)

# 홀수의 갯수가 2이상
if cnt_odd >= 2:
    print("I'm Sorry Hansoo")
else:
    print(palindrome_half+odd_str+palindrome_half[::-1])
