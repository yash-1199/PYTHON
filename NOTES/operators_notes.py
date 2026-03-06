"""Python Operators - Quick Notes with Examples"""

# 1. Arithmetic operators
x = 10
y = 3

print(x + y)   # 13 (Addition)
print(x - y)   # 7  (Subtraction)
print(x * y)   # 30 (Multiplication)
print(x / y)   # 3.333... (Division)
print(x % y)   # 1  (Modulus - remainder)
print(x ** y)  # 1000 (Exponent)
print(x // y)  # 3  (Floor division)

# 2. Comparison operators
print(x == y)  # False
print(x != y)  # True
print(x > y)   # True
print(x < y)   # False
print(x >= y)  # True
print(x <= y)  # False

# 3. Assignment operators
a = 5
a += 2   # a = a + 2 -> 7
a -= 1   # a = a - 1 -> 6
a *= 3   # a = a * 3 -> 18
a /= 2   # a = a / 2 -> 9.0
a %= 4   # a = a % 4 -> 1.0

# 4. Logical operators
p = True
q = False

print(p and q)  # False
print(p or q)   # True
print(not p)    # False

# 5. Bitwise operators
m = 5   # 0101
n = 3   # 0011
print('hi')
print(m & n)    # 1  (AND)
print(m | n)    # 7  (OR)
print(m ^ n)    # 6  (XOR)
print(~m)       # -6 (NOT)
print(m << 1)   # 10 (Left shift)
print(m >> 1)   # 2  (Right shift)

