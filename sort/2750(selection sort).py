n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

// 선택정렬

for i in range(n):  # 배열의 수만큼 반복
    min_index = i   # 최소값을 첫번째 값으로 설정
    for j in range(i + 1, n):
        if array[min_index] > array[j]:  # 가장 작은 수의 인덱스를 찾기
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]


for i in array:
    print(i)
