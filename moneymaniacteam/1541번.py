str = input().split('-')
result = []

for i in range(len(str)):
    if not str[i].isalnum():
        temp = str[i].split("+")
        temp = list(map(int, temp))
        result.append(sum(temp))

    else:
        str[i] = int(str[i])
        result.append(str[i])

hap = result[0]

for i in range(1, len(result)):
    hap -= result[i]
print(hap)
