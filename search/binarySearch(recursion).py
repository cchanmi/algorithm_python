array = [1, 3, 5, 6, 7, 9, 11, 20, 30]

def binarySearch(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  if array[mid] == target:
    return mid
  elif array[mid] > target:                             # 중간값보다 타겟값이 크다면
    return binary_search(array, target, start, mid-1)   # 중간값 -1의 값까지 다시 탐색 시작
  else:                                                 # 중간값보다 타겟값이 작다면
    return binary_search(array, target, mid+1 end)      # 중간값 + 1의 값부터 다시 탐색 시작
  
  
result = binarySearch(array, 5, 0, len(array) -1)
if result == None:
  print("탐색 실패")
else:
  print(result+1)
