## random module
import random

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random() * 5
print(random_float)


## List
fruits = ["Cherry", "Apple", "Pear"]
print(fruits)
print(fruits[1])
print(fruits[-1]) # prints the last item in the list
# -ve position counts from the end of the list

fruits[1] = "Peach"
print(fruits)

fruits.append("Grapes") # adds the item to the end of the list
print(fruits)

fruits.extend(["Orange", "Blackberry"]) # adds multiple items to the end of the list
print(fruits)

## nested list

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)