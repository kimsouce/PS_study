n = int(input())
A = input().split()
A.sort()  #이진탐색 하기 전 반드시 정렬
m = int(input())
array_M = input().split()

def binary_search(array, target, start, end):
  while start <= end:
    mid = (start+end) //2
    if array[mid] == target:
      return mid
    elif array[mid] < target:
      start = mid+1
    else:
      end = mid -1
  return None

for i in array_M:
  result = binary_search(A, i, 0, n-1)
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
