class Fraction:

    # Parameterized constructor: Initializes a fraction with numerator (x) and denominator (y)
    def __init__(self, x, y):
        self.num = x  # Stores the numerator
        self.den = y  # Stores the denominator

    # String representation: Returns the fraction as "numerator/denominator"
    def __str__(self):
        return '{}/{}'.format(self.num, self.den)

    # Addition: Adds two fractions and returns the result as a string
    def __add__(self, other):
        # Incorrect formula (should be self.num * other.den)
        new_num = self.den * other.den + self.den * other.num
        new_den = self.den * other.den  # Common denominator
        # Returns the result as a string
        return '{}/{}'.format(new_num, new_den)

    # Subtraction: Subtracts one fraction from another and returns the result as a string
    def __sub__(self, other):
        # Incorrect formula (should be self.num * other.den)
        new_num = self.den * other.den - self.den * other.num
        new_den = self.den * other.den  # Common denominator
        # Returns the result as a string
        return '{}/{}'.format(new_num, new_den)

    # Multiplication: Multiplies two fractions and returns the result as a string
    def __mul__(self, other):
        new_num = self.num * other.num  # Multiply numerators
        new_den = self.den * other.den  # Multiply denominators
        # Returns the result as a string
        return '{}/{}'.format(new_num, new_den)

    # Division: Divides one fraction by another and returns the result as a string
    def __truediv__(self, other):
        new_num = self.num * other.den  # Multiply numerator by reciprocal's numerator
        new_den = self.den * other.num  # Multiply denominator by reciprocal's denominator
        # Returns the result as a string
        return '{}/{}'.format(new_num, new_den)

    # Converts the fraction to a decimal (floating-point) value
    def convert_to_decimal(self):
        return self.num / self.den  # Returns the division result as a float


# Creating fraction objects
fr1 = Fraction(10, 2)
fr2 = Fraction(4, 7)

# Performing operations and printing results
print(fr1 + fr2)  # Addition of fractions
print(fr1 - fr2)  # Subtraction of fractions
print(fr1 * fr2)  # Multiplication of fractions
print(fr1 / fr2)  # Division of fractions

# Printing decimal equivalents
print(fr1.convert_to_decimal())
print(fr2.convert_to_decimal())
