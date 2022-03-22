if __name__ == '__main__':
    def mcss2(a):
        n = len(a)
        max_value = 0
        for i in range(0, n+1):
            current_value = 0
            for j in range(i, n):   # 왜 n일까? -> 합이기 때문에 n-1 = n이라고 적어야 함.
                current_value += a[j]
                if current_value > max_value:
                    max_value = current_value
        return max_value

    data = [-7, 4, -3, 6, 3, -8, 3, 4]
    result = mcss2(data)
    print(result)
