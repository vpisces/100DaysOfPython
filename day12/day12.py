## Scope

# enemies = 1
#
#
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
#
#
# increase_enemies()
#
# print(f"enemies outside function: {enemies}")


## If block does not have scope
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
#
# if game_level < 5:
#     new_enemy = enemies[0]

# print(new_enemy)


# if we put this if block inside a function, we cannot use the variable defined under if block outside of the function
def create_enemy():
    if game_level < 5:
        new_enemy = enemies[0]

#print(new_enemy)


## modifying global scope
# enemies = 1
#
#
# def increase_enemies():
#     global enemies
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
#
#
# increase_enemies()
#
# print(f"enemies outside function: {enemies}")
# Modifying global scope inside a function is not recommended


# Alternative to modify global scope variables

enemies = 1


# define a function and return a value
def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1


# call the function and assign the value to the global scope variable
enemies = increase_enemies()

print(f"enemies outside function: {enemies}")


# Global constants

PI = 3.14
# Naming convention: UPPERCASE

