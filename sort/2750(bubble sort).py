n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

for i in range(len(array) -1, 0, -1):
    for j in range(i):
        if array[j] > array[j+1]:
            array[j+1], array[j] = array[j], array[j+1]

for i in array:
    print(i)
