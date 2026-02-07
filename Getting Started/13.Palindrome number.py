def pali(n):
    rev=0
    dup=n
    while n>0:
        ld=n%10
        n=n//10
        rev=rev*10+ld
    if dup==rev:
        print('palindrome')
    else:
        print('not a palindrome')
n=int(input('enter the number'))
pali(n)