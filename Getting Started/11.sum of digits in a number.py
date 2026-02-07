def sum_of_digits_of_a_number(n):
    sum=0
    while n>0:
        ld=n%10
        sum=sum+ld
        n=n//10
    print(sum)
n=int(input("enter the number"))
sum_of_digits_of_a_number(n)