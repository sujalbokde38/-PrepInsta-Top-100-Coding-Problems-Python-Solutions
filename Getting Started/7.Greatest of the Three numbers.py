#Greatest of the Three numbers
def Greatest_of_the_Three_numbers(a, b, c):
    if a >= b and a >= c:
        print("a is greatest")
    elif b >= a and b >= c:
        print("b is greatest")
    else:
        print("c is greatest")

a = int(input("enter the number 1: "))
b = int(input("enter the number 2: "))
c = int(input("enter the number 3: "))

Greatest_of_the_Three_numbers(a, b, c)
