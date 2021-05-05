num = int(input())

triangle = []

for i in range(num):
    triangle.append(list(map(int, input().split())))

for i in range(1,num):
    for j in range(len(triangle[i])):
        if j == 0:
            triangle[i][j] = triangle[i][j] + triangle[i-1][j]
        elif j == i:
            triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
        else:
            triangle[i][j] = max(triangle[i][j]+triangle[i-1][j], triangle[i][j]+triangle[i-1][j-1])

print(max(triangle[num-1]))