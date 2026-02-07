#Greatest of two numbers: 
def Greatest_of_two_numbers(m,n):
    if n>m:
        print("1st number is greater",n)
    else:
        print("2nd number is greater",m) 
n=int(input("enter the 1st no"))
m=int(input("enter the 2nd no"))
Greatest_of_two_numbers(m,n)