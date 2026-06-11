a = 31
t = type(a) # class <int?

print(t) # <class 'int'>

b = 3.14
print(type(b)) # <class 'float'>

c = "Hello, World!"
print(type(c)) # <class 'str'>

d = False
print(type(d)) # <class 'bool'>

j = "31.24"
print(type(j)) # <class 'str'>

i = float(j) # Convert string to float
print(i) # 31.24
print(type(i)) # <class 'float'>