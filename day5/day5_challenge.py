## Average height

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

total_height = 0
total_student = 0
for h in student_heights:
    total_height += h
    total_student += 1

average_height = round(total_height/total_student)
print(average_height)


## Maximum Score

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
maximum_score = 0
for score in student_scores:
    if score > maximum_score:
        maximum_score = score

print(f"The highest score in the class is: {maximum_score}")

## Sum of even numbers from range 1 to 100

#Write your code below this row 👇
total = 0
for i in range(1, 101):
    if i % 2 == 0:
        total += i
print(total)


## Fizz Buzz

#Write your code below this row 👇

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

