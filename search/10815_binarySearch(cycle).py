import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
m = int(input())
card2 = list(map(int, input().split()))
card.sort()

def binary_search(target):
    low, high = 0, len(card)-1
    while low <= high:              # low값이 high 값보다 크거나 같을 때까지 반복
        middle = (low + high) // 2
        if target == card[middle]:
            return 1
        elif target < card[middle]: # 타겟값이 중간값보다 작을 경우
            high = middle -1        # high의 값이 중간값 -1로 바뀜
        elif target > card[middle]:
            low = middle + 1
    return 0                        # 값이 없을 경우 0 리턴
$
for i in card2:
    print(binary_search(i), end=' ')
