## Data types

# String
print("Hello"[0])

print("123" + "345")

# Integer
print(123 + 345)
print(123_456_789)
print(123_456_789 + 2)

# Float
print(3.14)

# Boolean
True
False

print(True)

# Type
num_char = len(input("What is your name?"))
# print("your name has " + num_char + " characters.")
    # TypeError: can only concatenate str (not "int") to str
new_num_char = str(num_char)
print(new_num_char)


a = 123
print(type(a)) #<class 'int'>

# Type Conversion
b = float(123)
print(type(b))

print(70 + float("100.5"))

print(str(70) + str(100))

# Mathematical Operations
# PEMDAS (Parenthesis Exponentiation Multiplication Division Addition Substraction)
# ()
# **
# * / -> priority from left to right
# + - -> priority from left to right

print(3 * 3 + 3 / 3 - 3)


## Number Manipulation
# Rounding
print(round(8/3))
print(round(8/3 , 2)) # Round up to two decimal places

score = 0
score += 1
print(score)

# F_Strings
score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

# print("Your score is " + score) // TypeError: can only concatenate str (not "int") to str