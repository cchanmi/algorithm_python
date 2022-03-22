if __name__ == '__main__':
    def get_max_profit2(a):
        n = len(a)
        max_profit = 0
        for i in range(0, n+1):
            current_profit = 0
            for j in range(i+1, n):
                current_profit = a[j] - a[i]
                if current_profit > max_profit:
                    max_profit = current_profit
        return max_profit

    data = [8, 1, 5, 3, 7, 4]
    result = get_max_profit2(data)
    print(result)
