import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no: 'Complex') -> 'Complex':
        return Complex(self.real + no.real, self.imaginary + no.imaginary)
        
    def __sub__(self, no: 'Complex') -> 'Complex':
        return Complex(self.real - no.real, self.imaginary - no.imaginary)
        
    def __mul__(self, no: 'Complex') -> 'Complex':
        real = self.real * no.real - self.imaginary * no.imaginary
        imaginary = self.real * no.imaginary + self.imaginary * no.real
        return Complex(real, imaginary)

    def __truediv__(self, no: 'Complex') -> 'Complex':
        real = (self.real * no.real + self.imaginary * no.imaginary) / (no.real ** 2 + no.imaginary ** 2)
        imaginary = (self.imaginary * no.real - self.real * no.imaginary) / (no.real ** 2 + no.imaginary ** 2)
        return Complex(real, imaginary)

    def mod(self) -> 'Complex':
        real = (self.real ** 2 + self.imaginary ** 2) ** 0.5
        imaginary = 0
        return Complex(real, imaginary)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result