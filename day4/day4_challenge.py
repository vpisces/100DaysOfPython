## banker roullete
import random

names_string = input("Give me the names, separated by comma.")
names = names_string.split(",")
length = len(names)
random_choice = random.randint(0, length - 1)
print(f"{names[random_choice]} is going to buy the meal today!")
#person = random.choice(names)
#print(f"{person} is going to buy the meal today!")


## Treasure Map
# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

column = int(position[0])
row = int(position[1])

selected_row = map[row - 1]
selected_row[column - 1] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

