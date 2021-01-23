word = input().lower()  #모두 소문자로 받아준다
count = 0
word_list = []
count_list = []

for w in word:
  if w not in word_list:
    word_list.append(w)   #중복값 없이 알파벳 리스트 생성


for i in word_list:
  for j in range(len(word)):
    if i == word[j]:
      count +=1   #각 알파벳의 출현 횟수를 세어줌
  count_list.append(count)   
  count = 0   # 같지 않을 경우 초기화

result = max(count_list)
if count_list.count(result) >=2:  #만약 최댓값이 2개이면
  print('?')
else:
  print(word_list[count_list.index(result)].upper())  #count_list의 최댓값의 인덱스를 추출하고, 그 위치에 해당하는 word_list의 원소값을 대문자로 반환
