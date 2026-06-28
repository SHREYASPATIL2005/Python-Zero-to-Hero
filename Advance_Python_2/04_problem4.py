
# 4. Write a program to filter a list of numbers which are divisible by 5.

def isDivisibleBy5(n):
    if(n % 5 == 0):
        return True
    return False

a = [1,2,418703,389819,92,75,30,50,100,4987,980,200,300,3289,400,500]
onlyDivisibleBy5 = list(filter(isDivisibleBy5, a))
print(onlyDivisibleBy5)  # Output: [75, 30, 50, 100, 200, 300, 400, 500]