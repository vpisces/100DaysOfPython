#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill?"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15?"))
total_people = int(input("How many people to split the bill?"))

bill_per_person = (total_bill / total_people) * ((100 + tip)/100)
#final_amount = round(bill_per_person, 2) // In case where the result is whole number,
# it will display only 1 digit after the decimal
final_amount = "{:.2f}".format(bill_per_person) # formatted to display 2 decimal places
print(f"Each person should pay: ${final_amount}")