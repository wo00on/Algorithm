a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

result1 = (a + b) % c
result2 = ((a % c) + (b % c)) % c
result3 = (a * b) % c
result4 = ((a % c) * (b % c)) % c

print(result1)
print(result2)
print(result3)
print(result4)