programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieving items from dictionary
print(programming_dictionary["Function"])

# Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# Create an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])



## Nested Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijio"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}
print(travel_log)
## Nested List
nested_list = ["A", "B", ["C", "D"]]
print(nested_list)

## Nesting Dictionary in a Dictionary
travel = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijio"],
        "total_visits":12
    },
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

print(travel)


## Nesting a Dictionary in a list
travel_log_list = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijio"],
        "total_visits":12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
]