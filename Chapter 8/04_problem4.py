'''
sum(1) = 1
sum(2) = 1 + 2 = 3
sum(3) = 1 + 2 + 3 = 6
... and so on.
sum(n) = 1 + 2 + 3 + ... + n
sum(n) = n + sum(n-1)
'''

def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n - 1)
    
n = int(input("Enter a number to calculate the sum of first n natural numbers: "))
print(f"The sum of first {n} natural numbers is {sum(n)}.")