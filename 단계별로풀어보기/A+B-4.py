""""while True:
    a, b = map(int, input().split())

    if a < 0 or b > 10:
        break

    print(a+b)

    print('------------------------------------------')
"""
while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        print("오류류")
