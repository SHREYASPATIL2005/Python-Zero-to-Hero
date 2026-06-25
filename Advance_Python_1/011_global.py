a = 89
b = 90

def fun():
    global a  # This line tells Python that we are referring to the global variable 'a' defined outside the function.
    a = 20
    b = 30 
    print(b)

fun()
print(a)  # Output: 20
print(b)  # Output: 90



