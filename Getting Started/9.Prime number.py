#Prime number
# the number thaat is divisible by itself and 1
def Prime_number(n):
    if n%n==0 and n%1==n:
        print("prime number")
    else:
        print('not a prime number')
n = int(input("Enter a number: "))
Prime_number(n)