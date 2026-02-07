def sumN(n):
    a = 0
    if n <= 0:
        print("Invalid input")
        return

    for i in range(1, n + 1):
        a += i

    print(a)

n = int(input("Enter a number: "))
sumN(n)
