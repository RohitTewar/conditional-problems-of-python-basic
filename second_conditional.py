# This program calculates the ticket price based on age and day of the week.

age = int(input("Enter your age: "))
day = str(input("entrer the day: "))

price = 120 if age>= 18 else 80

if day == "wednesday":
    price = price-20

print(f"Ticket price is {price}")