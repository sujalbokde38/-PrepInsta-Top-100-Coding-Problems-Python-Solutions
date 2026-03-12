def print_prime_factors(n):
    if n <= 1:
        print("No prime factors")
        return

    factors = []

    while n % 2 == 0:
        factors.append(2)
        n //= 2

    divisor = 3
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 2

    if n > 2:
        factors.append(n)

    print(*factors)


number = int(input("Enter a number: "))
print_prime_factors(number)
