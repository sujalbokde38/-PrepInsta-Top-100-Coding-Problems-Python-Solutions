def factorial(n):
    if n < 0:
        print("Factorial is not defined for negative numbers")
        return

    result = 1
    for i in range(2, n + 1):
        result *= i

    print(result)


n = int(input("Enter a number: "))
factorial(n)
