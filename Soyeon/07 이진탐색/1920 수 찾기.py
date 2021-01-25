n = int(input())
A = input().split()
A.sort()  #이진탐색 하기 전 반드시 정렬
m = int(input())
array_M = input().split()

def binary_search(array, target, start, end):
  while start <= end:
    mid = (start+end) //2   
    if array[mid] == target:  
      return mid     #해당 정수 찾은 경우 인덱스 반환
    elif array[mid] < target:
      start = mid+1  #target보다 중간값이 작은 경우, 중간값 뒤 쪽만 확인하면 됨
    else:
      end = mid -1   #target보다 중간값이 큰 경우, 중간값 앞 쪽만 확인하면 됨
  return None

for i in array_M:
  result = binary_search(A, i, 0, n-1)     #주어진 M개의 수 들이 리스트 A에 있는지 확인
  if result != None:
    print('1', sep='/n')
  else:
    print('0', sep='/n')
    
    
 '''
 #시간 초과 코드
n = int(input())
A = input().split()
m = int(input())
array = input().split()

for i in array:
  if i in A:
    print('1', sep='/n')
  else:
    print('0',sep='/n')
''' 
