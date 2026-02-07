def checkno(n):
    if n ==0:
        print('the number is zero',n)
    elif n>0:
        print('the number is a positive number',n)
    else:
        print("the number is a negative number",n)

n=int(input('enter the number'))
checkno(n)
