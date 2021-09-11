n = [9, 5, 8, 3, 7]

def seqSearch(key, low, high)
  for i in range(low, high+1):  # 배열의 처음부터 마지막까지 검사
    if a[i] == key:             # 찾으려는 값과 배열의 값이 같다면
      return i                  # 그 값의 위치를 반환
    
  return -1                     # 찾으려는 값이 없다면 -1을 반환
