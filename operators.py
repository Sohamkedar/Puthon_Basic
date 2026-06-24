# there are eight types of operators in python
# 1. Arithmetic operators
# 2. Relational operators
# 3. Assignment operators
# 4. Logical operators
# 5. Bitwise operators
# 6. Membership operators
# 7. Identity operators
# 8. Comparison operators


# Arithmetic operators
# Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, etc. on numeric values.
# +, -, *, /, %, **, //
print("Arithmetic operators")
a=10
b=3
c=a+b   #addition
d=a-b   #subtraction
g=a%b   #modulus
e=a*b   #multiplication
h=a**b  #exponentiation
f=a/b   #division
i=a//b  #floor division

print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print("\n\n")

# 2. Relational operators
# Relational operators are used to compare the values of two operands. The result of a relational operation is either True or False.
# ==, !=, <, >, <=, >=
print("Relational operators")
a=10
b=20
print(a==b)  #equal to
print(a!=b)  #not equal to
print(a<b)   #less than
print(a>b)   #greater than
print(a<=b)  #less than or equal to
print(a>=b)  #greater than or equal to
print("\n\n")

# 3. Assignment operators
# Assignment operators are used to assign values to variables. The most common assignment operator is the equal sign (=), which assigns the value on the right to the variable on the left. There are also compound assignment operators that combine an arithmetic operation with assignment.
# =, +=, -=, *=, /=, %=, **=, //=
print("Assignment operators")
a=10
a+=5  # equivalent to a = a + 5
print(a)
a-=3  # equivalent to a = a - 3
print(a)
a*=2  # equivalent to a = a * 2
print(a)
a/=4  # equivalent to a = a / 4
print(a)
a%=3  # equivalent to a = a % 3
print(a)
a**=2  # equivalent to a = a ** 2
print(a)
a//=2  # equivalent to a = a // 2
print(a)
print("\n\n")

# 4. Logical operators
# Logical operators are used to combine conditional statements. They return True or False based on the evaluation
print("Logical operators")
a=True
b=False
print(a and b)  # logical AND
print(a or b)   # logical OR
print(not a)    # logical NOT
print("\n\n")

# 5. Bitwise operators
# Bitwise operators are used to perform bit-level operations on binary numbers. They operate on the individual bits of the operands.
# &, |, ^, ~, <<, >>
print("Bitwise operators")
a=10  # binary: 1010
b=4   # binary: 0100
print(a & b)  # bitwise AND
print(a | b)  # bitwise OR
print(a ^ b)  # bitwise XOR
print(~a)     # bitwise NOT
print(a << 1) # left shift
print(a >> 1) # right shift
print("\n\n")

# 6. Membership operators
# Membership operators are used to test whether a value is present in a sequence (like a list or a string)
print("Membership operators")
list1=[1,2,3,4,5]
print(3 in list1)    # True
print(6 not in list1) # True
print("\n\n")

# 7. Identity operators
# Identity operators are used to compare the memory locations of two objects. They return True if both objects refer to the same memory location, and False otherwise.
print("Identity operators")
a=10
b=10
print(a is b)  # True
print(a is not b)  # False
print("\n\n")

# 8. Comparison operators
# Comparison operators are used to compare two values. They return True or False based on the comparison.
print("Comparison operators")
a=10
b=20
print(a < b)   # True
print(a > b)   # False
print(a == b)  # False
print(a != b)  # True
print(a <= b)  # True
print(a >= b)  # False
print("\n\n")