n = [3, 6, 8, 2, 1, 9, 5]

def seqSearch(key, low, high)
  for i in range(low, high+1):
    if a[i] == key:
      return i
    
  return -1
