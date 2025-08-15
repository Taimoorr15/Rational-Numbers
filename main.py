from math import gcd
from rational_num import RationalNumber

# Assuming your RationalNumber class is already defined above this
# (with the fixes we talked about)

def run_tests():
    print("=== RATIONAL NUMBER TESTS ===\n")

    # Create rational numbers
    r1 = RationalNumber(1, 2)   # 1/2
    r2 = RationalNumber(3, 4)   # 3/4
    r3 = RationalNumber(-2, 6)  # should simplify to -1/3

    print("Initial Numbers:")
    print("r1 =", r1)
    print("r2 =", r2)
    print("r3 =", r3, "\n")

    # Addition
    print("Addition:")
    print(f"{r1} + {r2} = {r1.add(r2)}")
    print(f"{r1} + {r3} = {r1.add(r3)}\n")

    # Subtraction
    print("Subtraction:")
    print(f"{r1} - {r2} = {r1.sub(r2)}")
    print(f"{r2} - {r3} = {r2.sub(r3)}\n")

    # Multiplication
    print("Multiplication:")
    print(f"{r1} * {r2} = {r1.multiply(r2)}")
    print(f"{r2} * {r3} = {r2.multiply(r3)}\n")

    # Division
    print("Division:")
    print(f"{r1} / {r2} = {r1.divide(r2)}")
    print(f"{r2} / {r3} = {r2.divide(r3)}\n")

    # Edge Case: Zero denominator (should raise error)
    print("Zero Denominator Check:")
    try:
        r_error = RationalNumber(5, 0)
    except ValueError as e:
        print("Caught error as expected:", e)

    # Edge Case: Division by zero numerator
    print("\nDivision by Zero Numerator Check:")
    try:
        r_zero = RationalNumber(0, 1)
        print(r1.divide(r_zero))
    except ZeroDivisionError as e:
        print("Caught error as expected:", e)

if __name__ == "__main__":
    run_tests()
