from math import gcd

class RationalNumber:
    def __init__(self,numerator:int,denominator:int):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")

        elif denominator < 0:
            numerator, denominator = -numerator, -denominator
        
        hcf = gcd(numerator,denominator)
        self._numerator = numerator // hcf
        self._denominator = denominator // hcf

    @property
    def numerator(self):
        return self._numerator    
    
    @numerator.setter
    def numerator(self, new_num):
        if self._numerator != new_num:
            self._numerator = new_num
        else:
            return self._numerator
        
    @property
    def denominator(self):
        return self._denominator
    
    @denominator.setter
    def denominator(self, new_den):
        if self._denominator != new_den:
            self._denominator = new_den
        else:
            return self._denominator
        
    def add(self, other):
        num = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        den = self.denominator * other.denominator
        return RationalNumber(num, den)
    
    def sub(self, other):
        num = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        den = self.denominator * other.denominator
        return RationalNumber(num, den)
    
    def multiply(self, other):
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        return RationalNumber(num, den)
    
    def divide(self, other):
        if other.numerator == 0:
            raise ZeroDivisionError("Denominator Cannot Be Zero")

        num = self.numerator * other.denominator
        den = self.denominator * other.numerator
        return RationalNumber(num, den)

    def __str__(self):
        return f"{self.numerator}" if self.denominator == 1 else f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"Rational Number(Numerator: {self.numerator}, Denominator: {self.denominator})"        
