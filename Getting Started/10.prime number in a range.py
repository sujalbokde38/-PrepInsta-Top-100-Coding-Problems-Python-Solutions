def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def print_primes_in_range(start, end):
    if start > end:
        start, end = end, start

    primes = []
    for value in range(start, end + 1):
        if is_prime(value):
            primes.append(value)

    if primes:
        print(*primes)
    else:
        print("No prime numbers in the given range")


start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
print_primes_in_range(start, end)
