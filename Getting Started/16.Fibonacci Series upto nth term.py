def fibonacci_upto_n_terms(n):
    if n <= 0:
        print("Please enter a positive number of terms")
        return

    a, b = 0, 1
    series = []

    for _ in range(n):
        series.append(a)
        a, b = b, a + b

    print(*series)


terms = int(input("Enter number of terms: "))
fibonacci_upto_n_terms(terms)
