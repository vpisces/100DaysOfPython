## Function with inputs

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("Faiyaz")

# Function with multiple parameters
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Faiyaz", "London")

# Function with keyword arguments
greet_with(name="Faiyaz", location="Dubai")
greet_with(location="Dubai", name="Faiyaz")
    # Result of both the function call will be same, order of the parameters doesn't matter in case of keyword arguments
    # name of the keyword in function call and defined function must match


## Prime Number

#Write your code below this line 👇

def prime_checker(number):
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            is_primerime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")



#Write your code above this line 👆

#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)