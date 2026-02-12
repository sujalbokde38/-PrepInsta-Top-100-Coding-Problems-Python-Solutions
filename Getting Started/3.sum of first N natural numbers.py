def sumN(n): #defined a function named sum
    a = 0
    if n <= 0: #edge case for negative number and zero
        print("Invalid input")
        return

    for i in range(1, n + 1): #logic
        a += i

    print(a)

n = int(input("Enter a number: "))
sumN(n)

