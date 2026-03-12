def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    total = 0

    for digit in digits:
        total += int(digit) ** power

    return total == num


def print_armstrong_in_range(start, end):
    if start > end:
        start, end = end, start

    armstrong_numbers = []
    for value in range(start, end + 1):
        if is_armstrong(value):
            armstrong_numbers.append(value)

    if armstrong_numbers:
        print(*armstrong_numbers)
    else:
        print("No Armstrong numbers in the given range")


start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
print_armstrong_in_range(start, end)
