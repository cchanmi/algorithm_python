n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

for i in range(len(array) -1, 0, -1):
    for j in range(i):              # 0부터 n-1까지
        if array[j] > array[j+1]:   # i번째 원소가 i+1보다 클 때
            array[j+1], array[j] = array[j], array[j+1]   # 값을 교환해 준다

for i in array:
    print(i)
