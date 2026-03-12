def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    total = 0

    for digit in digits:
        total += int(digit) ** power

    return total == num


n = int(input("Enter a number: "))
if is_armstrong(n):
    print("Armstrong number")
else:
    print("Not an Armstrong number")
