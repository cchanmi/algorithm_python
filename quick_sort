array = [3, 10, 5, 22, 1, 5, 6, 2, 78]

def quick_sort(array):
    if len(array) <= 1:
        return array;
    pivot = array[len(array) // 2]
    start, end, equal = [], [], []
    
    for num in array:
        if num < pivot:
            start.append(num)
        elif num > pivot:
            end.append(num)
        else:
            equal.append(num)
    return quick_sort(start) + equal + quick_sort(end)

print(quick_sort(array))
