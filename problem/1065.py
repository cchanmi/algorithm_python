def hansoo_number(number):
    count = 0
    for i in range(1, number + 1):
        if 1 <= i < 100:
            count += 1
        elif i == 1000:
            pass
        else:
            l = list(map(int, str(i)))
            if l[1] == (l[0] + l[2]) / 2:
                count += 1
    return count

number = int(input())
print(hansoo_number(number))
