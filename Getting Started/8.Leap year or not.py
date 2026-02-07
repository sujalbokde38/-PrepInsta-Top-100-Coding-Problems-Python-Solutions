# Leap year or not
def leap_year(n):
    # Rule 1: 400 se divisible year hamesha leap year hota hai
    if n % 400 == 0:
        print("leap year", n)

    # Rule 2: 100 se divisible year leap year nahi hota
    elif n % 100 == 0:
        print("not a leap year", n)

    # Rule 3: 4 se divisible year leap year hota hai
    elif n % 4 == 0:
        print("leap year", n)

    # Baaki sab normal year hote hain
    else:
        print("not a leap year", n)

n = int(input("enter the year: "))
leap_year(n)
