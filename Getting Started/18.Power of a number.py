def power(base, exponent):
    result = 1

    if exponent < 0:
        for _ in range(-exponent):
            result *= base
        result = 1 / result
    else:
        for _ in range(exponent):
            result *= base

    print(result)


base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))
power(base, exponent)
