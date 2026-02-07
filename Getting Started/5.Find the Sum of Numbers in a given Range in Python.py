def sum_of_number_for_given_range(n,m):
    sum=0
    if n>m:
        n,m=m,n
    for i in range(n,m+1):
        sum=sum+i
    print("sum of numbers:",sum)
n=int(input("enter the 1st no"))
m=int(input("enter the 2nd no"))
sum_of_number_for_given_range(n,m)

