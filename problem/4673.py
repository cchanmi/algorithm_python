natural_number = set(range(1, 10000))
construtor_number = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    construtor_number.add(i)

self_number = sorted(natural_number - construtor_number)

for i in self_number:
    print(i)
