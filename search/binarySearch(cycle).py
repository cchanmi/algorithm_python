import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
m = int(input())
card2 = list(map(int, input().split()))
card.sort()

def binary_search(target):
    low, high = 0, len(card)-1
    while low <= high:
        middle = (low + high) // 2
        if target == card[middle]:
            return 1
        elif target < card[middle]:
            high = middle -1
        elif target > card[middle]:
            low = middle + 1
    return 0

for i in card2:
    print(binary_search(i), end=' ')
