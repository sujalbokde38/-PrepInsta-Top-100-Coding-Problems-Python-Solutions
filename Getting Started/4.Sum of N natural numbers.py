def sum_of_natural_number(n):
    sum=0
    if n ==0:
        print("invalid number:enter a natural number")
        return
    for i in range(1,n+1):
        sum=sum+i
    print("sum of n natural number",sum)
n=int(input('enter the number'))
sum_of_natural_number(n)