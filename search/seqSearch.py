n = [9, 5, 8, 3, 7]

def seqSearch(key, low, high)
  for i in range(low, high+1):
    if a[i] == key:
      return i
    
  return -1
