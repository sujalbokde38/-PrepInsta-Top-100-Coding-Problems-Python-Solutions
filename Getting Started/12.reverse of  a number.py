def reverse_of_a_number(n):
    rev=0
    while n>0:
        ld=n%10
        n=n//10
        rev=(rev*10)+ld
    print(rev)
n = int(input("Enter a number: "))
reverse_of_a_number(n)
"""num = 1234
# Convert to string, reverse the string, convert back to int
reversed_num = int(str(num)[::-1])
print(reversed_num) # Output: 4321"""