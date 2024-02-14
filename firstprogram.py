print("hello world")
print("this is my first program")
print("starting Data Analytics...")

#printing output in multiple lines
print("""first line
second line
third line""")

print("first line\nsecond line\nthird line")


#comments
# this is a single line comment

"""multiple line comments
see i said multiple lines"""

#variables
a = "hello world"
print(a)

#input
# name = input("ENTER YOUR NAME:")  #default input type is string
# age = int(input("ENTER YOUR AGE:")) #adding int to specify numeric
# height = float(input("ENTER YOUR HEIGHT:"))

# print("Name:",name,"\nAge:",age,"\nHeight:",height)
#
# calc = eval(input("enter any expression:"))  #can evalutuate python command and any mathematical expression
#
# print(calc)


#data types
name = "john"
age = 18

print("data type of ",name," is",type(name))
print("data type of ",age," is",type(age))

#implicit conversion
a = 12.3
b = 13
print("type of ",a," is",type(a))
print("type of ",b," is",type(b))
c = a + b
print("type of" , c , "is" , type(c))

#explicit conversion
a = "12.3"
b = 13
print("type of ",a," is",type(a))
print("type of ",b," is",type(b))
a = float(a)
print("type of ",a," is",type(a))
c = a + b
print("type of" , c , "is" , type(c))

#operators and operands

"""ARITHMETIC OPERATORS
ADD     +
SUB     -
MULTIPLY    *
DIV     /
FLOOR DIV   // 
EXPONENTIATION     **
MODULUS     %
"""

a = 10
b = 20

print("ARITHMETICS OPERATORS")
print("addition of", a,  "and ", b , "is ", a+b)
print("subtraction of", a,  "and ", b , "is ", a-b)
print("division of", a,  "and ", b , "is ", a/b)
print("multiplication of", a,  "and ", b , "is ", a*b)
print("floor division of", a,  "and ", b , "is ", a//b) #gives output before the decimal point
print("exponentiation of", a,  "and ", b , "is ", a**b)
print("modulus of", a,  "and ", b , "is ", a%b)

"""COMPARISION OPERATORS
less than   <
greater than    >
less than or equal to   <=
greater than or equal to    >=
equal to    ==
not equal to    !=
"""

print("3 < 6 ",3<6)
print("3 > 6 ",3>6)
print("3 == 6 ",3==6)
print("3 != 6 ",3!=6)
print("3 <= 6 ",3<=6)
print("3 >= 6 ",3>=6)


"""LOGICAL OPERATORS
and   returns TRUE if both the operands are true
or    returns TRUE if either of the operands is true
not   returns TRUE if operand is false"""

