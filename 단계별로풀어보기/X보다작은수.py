N, X = map(int, input().split())
line = list(map(int, input().split()))

for i in line:
    if i < X:
        print(i, end=" ")