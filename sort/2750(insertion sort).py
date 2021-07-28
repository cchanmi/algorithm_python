n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

 // 삽입정렬 코드

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

for i in array:
    print(i)
