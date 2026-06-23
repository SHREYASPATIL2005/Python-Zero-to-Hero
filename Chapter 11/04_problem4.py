class complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return complex(self.real + other.real, self.imag + other.imag)
    
    def __mul__(self, other):
        return complex(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)

    def __str__(self):
        return f"{self.real} + {self.imag}i"
    
c1 = complex(2, 3)
c2 = complex(4, 5)
print(c1 + c2) # 6 + 8i
print(c1 * c2) # -7 + 22i