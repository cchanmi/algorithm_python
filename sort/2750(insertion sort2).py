   def sort1(a):
        n = len(a)
        for i in range(1, n):
            x = a[i]
            j = i-1
            while j >= 0 and a[j] > x:
                a[j+1] = a[j]
                j -= 1
            a[j+1] = x

    number = int(input())
    array = []
    for i in range(1, number+1):
        array.append(int(input()))  # [5, 4, 3, 2, 1}

    sort1(array)    # [1, 2, 3, 4, 5]
