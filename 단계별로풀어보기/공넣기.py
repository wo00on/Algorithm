N, M = map(int, input().split())

line = [0] * N

for _ in range(M):
    i, j, k = map(int, input().split())

    for r in range(i-1, j):
        line[r] = k

for c in range(line):
    print(num, end="")
