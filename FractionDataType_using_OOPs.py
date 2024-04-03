class Fraction:
    
    def __init__(self,numerator,denominator):
        if denominator == 0:
            raise ValueError("Denominator Cannot Be Zero")
        self.num = numerator
        self.den = denominator

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self,*args):
        for i in args:
            new_num = self.num*i.den + i.num*self.den
            new_den = self.den*i.den
        return Fraction(new_num,new_den)

    def __sub__(self,*args):
        for i in args:
            new_num = self.num*i.den - i.num*self.den
            new_den = self.den*i.den
        return Fraction(new_num,new_den)

    def __mul__(self,*args):
        for i in args:
            new_num = self.num*i.num
            new_den = self.den*i.den
        return Fraction(new_num,new_den)
        
    def __truediv__(self,*args):
        for i in args:
            new_num = self.num*i.den
            new_den = self.den*i.num
        return Fraction(new_num,new_den)
        
    def gcd(self):
        a = self.den
        b = self.num
        while b!= 0:
            a, b =  b, a%b
            return a  
            
    def lcm(self): 
        lcm = abs(self.num*self.den)//self.gcd()
        return lcm

    def simplify(self):
        a = self.gcd()
        new_num = self.num//a
        new_den = self.den//a
        return f"{new_num}/{new_den}"

    def to_decimal(self):
        return round((self.num/self.den),2)

    def reciprocal(self):
        return f"{self.den}/{self.num}"