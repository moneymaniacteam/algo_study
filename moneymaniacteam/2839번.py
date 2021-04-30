


N = int(input())

result = 0

if N <= 4:
    if(N==3):
        print(1)
    else:
        print(-1)
elif N % 5 == 0:
    result = N//5
    print(result)
elif N % 5 == 3:
    result = N // 5 + 1
    print(result)
elif N - (5 * (N // 5 - 1)) == 6:
    result = (N // 5 - 1) + 2
    print(result)
elif N - (5 * (N // 5 - 1)) == 9:
    result = (N // 5 - 1) + 3
    print(result)
elif N // 5 - 2 >= 0 and N - (5 * (N // 5 - 2)) == 12:
    result = (N // 5 - 2) + 4
    print(result)
else:
    print(-1)





