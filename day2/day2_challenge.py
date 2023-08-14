
## Challenge 1
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
result = first_digit + second_digit

print(result)

## Challenge 2
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = int(weight) / (float(height) ** 2)
bim_as_integer = int(bmi)
print(bim_as_integer)
