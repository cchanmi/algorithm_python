   def insertion_sort(a):
        for i in range(1, len(a)):
            x = a[i]
            j = i-1
            while j >= 0 and a[j] > x:
                a[j+1] = a[j]
                j -= 1
            a[j + 1] = x


if __name__ == '__main__':
    data = [6,5, 6, 4, 3, 2, 1]
    insertion_sort(data)
    print(data)     # return 값이 없는 함수이기 때문에 정렬을 한 후, 값을 출력하니 none값이 나오던 오류를 해결했다.
