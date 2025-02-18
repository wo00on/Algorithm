T = int(input())

for _ in range(T):
    cnt, text = input().split()

    for i in text:
        print(i * int(cnt), end="")
    print()
  
   