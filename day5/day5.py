## FOR loop

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print(fruits)

## Built In Functions
nums = [1, 2, 3, 4, 8, 6, 5]
# sum()
sum_of_nums = sum(nums)
print(sum_of_nums)

# len()
size_of_list = len(nums)
print(size_of_list)

# max()
maximum_of_list = max(nums)
print(maximum_of_list)

# min()
minimum_of_list = min(nums)
print(minimum_of_list)

## FOR loop range

for number in range(1, 10): # does not include 10
    print(number)

for number in range (0, 10):
    print(number)

for number in range(10):
    print(number)

for number in range(1, 10, 3): # 3 is step
    print(number)

