

n = int(input())
tree = {}

for n in range(n):
    root, left, right = map(str, input().split())
    tree[root] = [left, right]  #dictionary 활용

def preOrder(root):
    if root != '.':
        print(root, end="")  #루트
        preOrder(tree[root][0])  #왼쪽자식
        preOrder(tree[root][1])  #오른쪽자식

def inOrder(root):
    if root != '.':
        inOrder(tree[root][0])
        print(root, end="")
        inOrder(tree[root][1])

def postOrder(root):
    if root != '.':
        postOrder(tree[root][0])
        postOrder(tree[root][1])
        print(root, end="")

preOrder("A")
print()
inOrder("A")
print()
postOrder("A")
