"""
N = int(input())

card = []

for i in range(N):
    card.append(int(input()))

card.sort()

temp = 0

for i in range(N-1):
    temp += card[i] + card[i+1]
    card[i+1] = temp

print(temp)
메모리초과 """

import heapq

N = int(input())
card = []
for _ in range(N):
    heapq.heappush(card, int(input()))

if len(card) == 1:
    print(0)
else:
    temp = 0
    while len(card) > 1:
        first = heapq.heappop(card)
        second = heapq.heappop(card)
        temp += first + second
        heapq.heappush(card, first + second)
    print(temp)

